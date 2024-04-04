from enum import Enum


class EmailType(str, Enum):
    password_reset = "password_reset"
    verification = "verification"
    welcome = "welcome"
