from exchange_cash.exchange import Exchange


class Cash:

    def __init__(self, cents: int, exchange: Exchange):
        self._exchange = exchange
        self._cents = cents

    @property
    def cents(self):
        return self._cents

    def in_(self, currency: str):
        return Cash(
            self._cents * self._exchange.rate('USD', currency),
            self._exchange
        )

    def to_string(self):
        return str(self._cents)
