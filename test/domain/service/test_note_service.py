from datetime import date
from src.domain.service.note_service import NoteService


class TestNoteService:

    def test_parse_easynvest(self) -> None:
        trading_note = NoteService.parse(
            "test/domain/service/files/Invoice_190011.pdf")

        assert trading_note.dict() == {
            "note_id": "190011",
            "broker": "NuInvest",
            "total_amount": 2309.21,
            "trading_date": date(2019, 12, 26),
            "liquidate_date": date(2019, 12, 30),
            "note_items": [
                {
                    "asset_code": "FOFT11",
                    "unit_price": 120.0,
                    "quantity": 10,
                    "operation": "C",
                    "total_amount": 1200.0,
                    "currency": "BRL"
                },
                {
                    "asset_code": "SDIP11",
                    "unit_price": 110.85,
                    "quantity": 10,
                    "operation": "C",
                    "total_amount": 1108.5,
                    "currency": "BRL"
                }
            ]
        }

    def test_parse_nuinvest(self) -> None:
        trading_note = NoteService.parse(
            "test/domain/service/files/Invoice_103226.pdf")

        assert trading_note.dict() == {
            "note_id": "103226",
            "broker": "NuInvest",
            "total_amount": 624.91,
            "trading_date": date(2022, 6, 3),
            "liquidate_date": date(2022, 6, 7),
            "note_items": [
                {
                    "asset_code": "CPTS11",
                    "unit_price": 94.60,
                    "quantity": 2,
                    "operation": "C",
                    "total_amount": 189.2,
                    "currency": "BRL"
                },
                {
                    "asset_code": "KNRI11",
                    "unit_price": 132.19,
                    "quantity": 3,
                    "operation": "C",
                    "total_amount": 396.57,
                    "currency": "BRL"
                },
                {
                    "asset_code": "MXRF11",
                    "unit_price": 9.74,
                    "quantity": 4,
                    "operation": "C",
                    "total_amount": 38.96,
                    "currency": "BRL"
                }
            ]
        }

    def test_parse_clear(self) -> None:
        trading_note = NoteService.parse(
            "test/domain/service/files/Invoice_19889017.pdf")

        assert trading_note.dict() == {
            "note_id": "19889017",
            "broker": "Clear",
            "total_amount": 58.65,
            "trading_date": date(2021, 12, 16),
            "liquidate_date": date(2021, 12, 20),
            "note_items": [
                {
                    "asset_code": "ENGIE BRASIL ON NM",
                    "unit_price": 38.93,
                    "quantity": 1,
                    "operation": "C",
                    "total_amount": 38.93,
                    "currency": "BRL"
                },
                {
                    "asset_code": "ITAUUNIBANCO ON N1",
                    "unit_price": 19.71,
                    "quantity": 1,
                    "operation": "C",
                    "total_amount": 19.71,
                    "currency": "BRL"
                }
            ]
        }
