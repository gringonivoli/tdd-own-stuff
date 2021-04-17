from abc import ABCMeta, abstractmethod


class Exchange(metaclass=ABCMeta):

    @abstractmethod
    def rate(self, origin_currency, target_currency):
        pass


class ExchangeFake(Exchange):
    def rate(self, origin_currency, target_currency):
        return 150 if origin_currency != target_currency else 1
