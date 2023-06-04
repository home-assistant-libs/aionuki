"""Aionuki."""
import asyncio
from typing import Any, Dict, List, Optional, Union, cast

import aiohttp
from yarl import URL
import hashlib
from datetime import datetime
from random import randint
import nacl.secret
import nacl.utils

from .exceptions import CannotConnect, NukiException, Unauthorized

class NukiBridge:
    """The Nuki bridge running the HTTP-API."""

    def __init__(
            self,
            websession: aiohttp.ClientSession,
            host: str,
            port: int = 8080,
            token: str,
            timeout: int = 10,
    ):
        self.websession: aiohttp.ClientSession = websession
        self._host: str = host
        self._port: int = port
        self._tokendigest: str = hashlib.sha256(token.encode("utf-8")).digest()
        self._timeout: aiohttp.ClientTimeout = aiohttp.ClientTimeout(total=timeout)
    
    @property
    def base_url(self) -> str:
        """Return the base URL for endpoints."""
        return f"http://{self._host}:{self._port}"
    
    async def _request(self, path: str) -> aiohttp.ClientResponse:
        """Make the actual request and return the parsed response."""
        url: str = f"{self.base_url}{path}"

        try:
            response = await self.websession.get(
                url, params=self.get_encrypted_token_params(), timeout=self._timeout, raise_for_status=True
            )
        
        except aiohttp.ClientResponseError as error:
            if error.status == 401:
                raise Unauthorized("Incorrect token") from error
            raise NukiException(
                f"code: {error.code}, error: {error.message}"
            ) from error
        except (asyncio.TimeoutError, aiohttp.ClientError) as error:
            raise CannotConnect(error) from error
        
        return response

    def get_encrypted_token_params(self) -> Dict[str, str]:
        """Returns the HTTP params for authentication."""
        nonce = nacl.utils.random(24)
        rnr = randint(0, 65535)
        ts = datetime.utcnow().strftime(f"%Y-%m-%dT%H:%M:%SZ,{rnr}")
        box = nacl.secret.SecretBox(self._tokendigest)
        ctoken = box.encrypt(ts.encode("utf-8"), nonce)
        return {"ctoken": str(ctoken.ciphertext.hex()), "nonce": str(nonce.hex())}