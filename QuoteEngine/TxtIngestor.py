from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TxtIngestor(IngestorInterface):
    allowed_extensions = ["txt"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:

        quotes = []

        with open(path, 'r') as txt_file:
            all_lines = txt_file.readlines()
            for line in all_lines:
                quote_split = line.split(" - ")
                new_quote = QuoteModel(quote_split[0], quote_split[1])
                quotes.append(new_quote)

        return quotes
