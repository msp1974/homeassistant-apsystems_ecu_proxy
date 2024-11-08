"""Constants."""

from enum import StrEnum

DOMAIN = "apsystems_ecu_proxy"

ATTR_TIMESTAMP = "timestamp"
ATTR_VALUE_IF_NO_UPDATE = "value_if_no_update"
ATTR_SUMMATION_PERIOD = "summation_period"
ATTR_SUMMATION_TYPE = "summation_type"
ATTR_SUMMATION_FACTOR = "summation_factor"
ATTR_CURRENT_VALUE = "value"
ATTR_INVERTERS = "inverters"


MESSAGE_EVENT = f"{DOMAIN}_message"

SOLAR_ICON = "mdi:solar-power"
FREQ_ICON = "mdi:sine-wave"
RELOAD_ICON = "mdi:reload"
CACHE_ICON = "mdi:cached"
RESTART_ICON = "mdi:restart"
DCVOLTAGE_ICON = "mdi:current-dc"
POWER_ICON = "mdi:power"

# Datacom handling
SOCKET_PORTS = [8995, 8996, 8997]
EMA_HOST = "3.67.1.32"
# Max age of message (in seconds) to process
MESSAGE_IGNORE_AGE = 1800
# Max summation stub time to add for new period - see code in summation_calculation method in
MAX_STUB_INTERVAL = 300
# Used to prevent sending data to EMA for testing purposes.  Set to false during testing.
SEND_TO_EMA = True

# Config flow schema. These are also translated through associated json translations
KEYS = [
            "ema_host", 
            "message_ignore_age", 
            "max_stub_interval", 
            "no_update_timeout", 
            "send_to_ema"
        ]


class SummationPeriod(StrEnum):
    """Summation period Enum."""

    HOURLY = "hourly"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"
    LIFETIME = "lifetime"


class SummationType(StrEnum):
    """Summation type Enum."""

    SUM = "sum"
    MAX = "max"
    MIN = "min"
