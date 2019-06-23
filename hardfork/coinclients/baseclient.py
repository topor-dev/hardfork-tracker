__all__ = ['BaseCoinClient']


class BaseCoinClient:
    def get_median_time_past(self) -> int:
        """Returns median time past of the most recent 11 blocks

        median time past (MTP) - https://en.bitcoin.it/wiki/Block_timestamp
        """
        raise NotImplementedError()
