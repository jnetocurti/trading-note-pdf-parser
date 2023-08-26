from datetime import date
import functools
from typing import List
from pydantic import BaseModel

from src.domain.model.trading_note_item import TradingNoteItem


class TradingNote(BaseModel):
    broker: str
    note_id: str
    total_amount: float
    trading_date: date
    liquidate_date: date
    note_items: List[TradingNoteItem]

    @property
    def liquid_total_amount(self):
        return functools.reduce(
            lambda ac, i: ac + i.total_amount, self.note_items, 0
        )

    @property
    def costs(self):
        return round((self.total_amount - self.liquid_total_amount), 6)

    @property
    def unit_cost_multiplier(self):
        return self.costs / self.liquid_total_amount
