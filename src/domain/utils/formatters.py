from datetime import date
from re import sub
from decimal import Decimal
from dateutil import parser


def currency_to_decimal(value: str, pattern: str = "BR"):
    if pattern == "BR":
        return Decimal(sub(r",", ".", sub(r"[^\d,]", "", value)))
    else:
        return Decimal(sub(r"[^\d.]", "", value))


def string_to_date(value: str, pattern: str = "BR"):
    if pattern == "BR":
        return parser.parse(value, dayfirst=True).date()
    else:
        return parser.parse(value).date()


def float_to_string(value: float, pattern: str = "BR"):
    if pattern == "BR":
        return sub(r"\.", ",", str(value))
    else:
        return str(value)


def format_date(value: date, format: str = "%d/%m/%Y"):
    return value.strftime(format)


def remove_spaces(value: str) -> str:
    return sub(r"\s{2,}", " ", value)
