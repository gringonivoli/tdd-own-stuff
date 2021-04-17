import requests
from exchange_cash.exchange import Exchange


class BinanceExchange(Exchange):

    def rate(self, origin_currency, target_currency) -> int:
        return requests.get('https://google.com').json()
