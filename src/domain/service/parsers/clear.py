import re
from src.domain.model.trading_note_item import TradingNoteItem
from src.domain.service.parsers.parser import Parser
from src.domain.utils.formatters import currency_to_decimal, string_to_date, remove_spaces


class Clear(Parser):

    broker = "Clear"
    currency = "BRL"

    @classmethod
    def get_note_id(cls, note_text):
        pattern = r"[Nr.nota\s]{10}([\d]+)"
        return re.search(pattern, note_text).group(1)

    @classmethod
    def get_trading_date(cls, note_text):
        pattern = r"[Datpregão\s]{13}([\d/]{10})"
        return string_to_date(re.search(pattern, note_text).group(1))

    @classmethod
    def get_liquidation_date(cls, note_text):
        pattern = r"[Líquidopar\s]{12}([\d/]{10})"
        return string_to_date(re.search(pattern, note_text).group(1))

    @classmethod
    def get_total_amount(cls, note_text):
        pattern = r"[OutrosC\s]{8}([\d.,]+)[Líquidopar\s]{14}[\d/]{10}"
        return currency_to_decimal(re.search(pattern, note_text).group(1))

    @classmethod
    def get_note_items(cls, note_text):

        # Pattern para obter o texto da tabela de items
        pattern = r"[AjusteD/C\s]{11}(.*)[NOTADEGCIÇÃ\s]{18}"
        note_items_text = re.search(pattern, note_text)

        assets = list()
        items_data = note_items_text.group(1).split("BOVESPA")[1:]

        # Pattern para obter os campos específicos dos items
        pattern = r"([CV]{1})[FRACION\s]{13}(.*)\s(\d)\s([\d.,]+)\s([\d.,]+)"

        for data in items_data:
            match = re.search(pattern, data)
            assets.append(TradingNoteItem(
                asset_code=remove_spaces(match.group(2)),
                unit_price=currency_to_decimal(match.group(4)),
                quantity=match.group(3),
                operation=match.group(1),
                total_amount=currency_to_decimal(match.group(5)),
                currency=cls.currency,
            ))

        return assets
