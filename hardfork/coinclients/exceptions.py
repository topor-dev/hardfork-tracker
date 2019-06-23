class BaseCoinClientException(Exception):
    pass


class CoinClientUnexpectedException(BaseCoinClientException):
    pass


__all__ = ['BaseCoinClientException', 'CoinClientUnexpectedException']
