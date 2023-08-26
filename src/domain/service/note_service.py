import re
from PyPDF2 import PdfReader
from src.domain.model.trading_note import TradingNote
from src.domain.service.parsers.clear import Clear
from src.domain.service.parsers.nuinvest import NuInvest


class NoteService:

    @staticmethod
    def parse(file_path: str) -> TradingNote:

        reader = PdfReader(file_path)

        note_text = re.sub("\n", " ", "".join(
            [page.extract_text(0) for page in reader.pages]))

        if "62.169.875/0001-79" in note_text:
            return NuInvest.parse(note_text)

        elif "02.332.886/0011-78" in note_text:
            return Clear.parse(note_text)

        else:
            raise RuntimeError(f"Unsuported trading note: {file_path}")
