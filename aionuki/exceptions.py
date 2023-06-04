"""Aionuki exceptions."""


class NukiException(Exception):
    """Base exception for Aionuki."""

class Unauthorized(NukiException):
    """Token is incorrect."""

class CannotConnect(NukiException):
    """Exception raised when failed to connect the bridge."""