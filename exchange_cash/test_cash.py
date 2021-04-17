from exchange_cash.cash import Cash
from exchange_cash.exchange import ExchangeFake


def test_cash():
    assert Cash(1, ExchangeFake())


def test_cash_cents():
    cents = 4
    dollar = Cash(cents, ExchangeFake())

    assert cents == dollar.cents


def test_cash_in_usd():
    cents = 4
    dollar = Cash(cents, ExchangeFake())

    assert '4' == dollar.in_('USD').to_string()


def test_cash_in_arg_pesos():
    cents = 4
    dollar = Cash(cents, ExchangeFake())

    assert '600' == dollar.in_('ARG').to_string()

