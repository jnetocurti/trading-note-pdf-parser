import abc
from datetime import date
from src.domain.model.trading_note_item import TradingNoteItem
from src.domain.model.trading_note import TradingNote


class Parser(abc.ABC):

    @classmethod
    def parse(cls, note_text) -> TradingNote:
        return TradingNote(
            broker=cls.broker,
            note_id=cls.get_note_id(note_text),
            total_amount=cls.get_total_amount(note_text),
            trading_date=cls.get_trading_date(note_text),
            liquidate_date=cls.get_liquidation_date(note_text),
            note_items=cls.get_note_items(note_text)
        )

    @abc.abstractproperty
    def broker(cls) -> str:
        raise NotImplementedError

    @abc.abstractproperty
    def currency(cls) -> str:
        raise NotImplementedError

    @abc.abstractclassmethod
    def get_note_id(cls, note_text: str) -> str:
        raise NotImplementedError

    @abc.abstractclassmethod
    def get_trading_date(cls, note_text: str) -> date:
        raise NotImplementedError

    @abc.abstractclassmethod
    def get_liquidation_date(cls, note_text: str) -> date:
        raise NotImplementedError

    @abc.abstractclassmethod
    def get_total_amount(cls, note_text: str) -> float:
        raise NotImplementedError

    @abc.abstractclassmethod
    def get_note_items(cls, note_text: str) -> TradingNoteItem:
        raise NotImplementedError
