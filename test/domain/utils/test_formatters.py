from datetime import date
from decimal import Decimal
from src.domain.utils.formatters import currency_to_decimal, string_to_date, format_date, float_to_string, remove_spaces


class TestFormatters:

    def test_currency_to_decimal(self) -> None:
        assert Decimal("1000.01") == currency_to_decimal("R$ 1.000,01")
        assert Decimal("1000.01") == currency_to_decimal("$ 1,000.01", "USA")

    def test_string_to_date(self) -> None:
        assert date(2022, 9, 3) == string_to_date("03/09/2022")
        assert date(2022, 9, 3) == string_to_date("09/03/2022", "USA")
        assert date(2022, 9, 3) == string_to_date("03-09-2022")
        assert date(2022, 9, 3) == string_to_date("09-03-2022", "USA")

    def test_float_to_string(self) -> None:
        assert "1000,01" == float_to_string(1000.01)
        assert "1000.01" == float_to_string(1000.01, "USA")

    def test_format_date(self) -> None:
        assert "03/09/2022" == format_date(date(2022, 9, 3))
        assert "03-09-2022" == format_date(date(2022, 9, 3), "%d-%m-%Y")

    def test_remove_spaces(self) -> None:
        assert (
            "ENGIE BRASIL ON NM" ==
            remove_spaces("ENGIE BRASIL          ON  NM")
        )
