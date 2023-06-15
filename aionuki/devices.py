"""Classes for Nuki devices."""
class NukiDevice:
    """Base class for Nuki devices."""

    def __init__(
            self,
            data
    ):
        self.data = data

    @property
    async def nuki_id(self) -> str:
        """ID of the Nuki device."""
        return self.data["nukiId"]

    # deviceType
    @property
    async def device_type(self) -> int:
        """Nuki device type."""
        return self.data["deviceType"]

    @property
    async def name(self) -> str:
        """Name of the Nuki device."""
        return self.data["name"]

    @property
    async def mode(self) -> int:
        """ID of the lock mode."""
        return self.data["lastKnownState"]["mode"]
    
    @property
    async def state(self) -> int:
        """ID of the lock state."""
        return self.data["lastKnownState"]["state"]
    
    @property
    async def state_name(self) -> str:
        """Name of the lock state."""
        return self.data["lastKnownState"]["stateName"]
    
    @property
    async def battery_critical(self) -> bool:
        """Flag indicating if the batteries of the Nuki device are at critical level."""
        return self.data["lastKnownState"]["batteryCritical"]
    
    @property
    async def battery_charging(self) -> bool:
        """Flag indicating if the batteries of the Nuki device are charging at the moment."""
        return self.data["lastKnownState"]["batteryCharging"]

    @property
    async def battery_charge_state(self) -> int:
        """Value representing the current charge status in %."""
        return self.data["lastKnownState"]["batteryChargeState"]
   
    @property
    async def keypad_battery_critical(self) -> bool:
        """Flag indicating if the batteries of the paired Nuki Keypad are at critical level."""
        return self.data["lastKnownState"]["keypadBatteryCritical"]
    
    @property
    async def doorsensor_state(self) -> int:
        """ID of the door sensor state."""
        return self.data["lastKnownState"]["doorsensorState"]
    
    @property
    async def doorsensor_state_name(self) -> str:
        """Name of the door sensor state."""
        return self.data["lastKnownState"]["doorsensorStateName"]
    
    @property
    async def ringaction_timestamp(self) -> str:
        """Timestamp of the last ring-action."""
        return self.data["lastKnownState"]["ringactionTimestamp"]

    @property
    async def ringaction_state(self) -> bool:
        """Flag indicating if a ring-action is currently occuring or not (reset after 30 seconds)."""
        return self.data["lastKnownState"]["ringactionState"]

    @property
    async def timestamp(self) -> str:
        """Timestamp of the retrieval of this lock state."""
        return self.data["lastKnownState"]["timestamp"]