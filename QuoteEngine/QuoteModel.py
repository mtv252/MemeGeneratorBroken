"""Defines a QuoteModel as an author/text body pairing"""

class QuoteModel():
    """A simple Quote Object."""

    def __init__(self, body, author):
        """Initialize the Quote object.

        :param body: The text content of the quote.
        :param author: The attributed author, if any.
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f'"{body}" - {author}'
