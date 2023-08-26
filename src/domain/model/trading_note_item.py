from pydantic import BaseModel


class TradingNoteItem(BaseModel):
    asset_code: str
    unit_price: float
    quantity: int
    operation: str
    total_amount: float
    currency: str
