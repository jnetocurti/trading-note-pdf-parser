import io
import csv
from src.domain.model.trading_note import TradingNote
from src.domain.utils.formatters import format_date, float_to_string


def to_json(note: TradingNote) -> str:
    return note.json()


def to_csv(note: TradingNote) -> str:
    fieldnames = [
        "note_id",
        "trade_date",
        "liquidate_date",
        "operation",
        "asset_code",
        "quantity",
        "unit_price",
        "costs",
        "total_amount",
    ]
    output = io.StringIO()
    writer = csv.DictWriter(output, delimiter=";", fieldnames=fieldnames)

    writer.writeheader()

    def costs(item_total_amount):
        return round(note.unit_cost_multiplier * item_total_amount, 6)

    def total_amount(item_total_amount):
        return round(item_total_amount + costs(item_total_amount), 6)

    [writer.writerow({
        fieldnames[0]: note.note_id,
        fieldnames[1]: format_date(note.trading_date),
        fieldnames[2]: format_date(note.liquidate_date),
        fieldnames[3]: i.operation,
        fieldnames[4]: i.asset_code,
        fieldnames[5]: i.quantity,
        fieldnames[6]: float_to_string(i.unit_price),
        fieldnames[7]: float_to_string(costs(i.total_amount)),
        fieldnames[8]: float_to_string(total_amount(i.total_amount))
    }) for i in note.note_items]

    return output.getvalue()
