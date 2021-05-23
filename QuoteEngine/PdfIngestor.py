from typing import List
import subprocess
import os
import random
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PdfIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:

        quotes = []

        tmp = f'./tmp/{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp], shell=True)

        with open(tmp, "r") as file_ref:
            quotes = []
            for line in file_ref.readlines():
                line = line.strip('/n/r').strip()
                if len(line) > 0:
                    parsed = line.split(',')
                    new_quote = QuoteModel(parsed[0], parsed[1])
                    quotes.append(new_quote)


        return quotes
