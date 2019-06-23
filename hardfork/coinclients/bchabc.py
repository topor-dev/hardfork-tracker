import json
import logging
from typing import Dict, List, Optional, Tuple, Union

import attr
import requests

from .baseclient import BaseCoinClient
from .exceptions import CoinClientUnexpectedException

__all__ = ['BitcoinCashABCClient']


class _PartitionDescriptor:
    def __get__(self, obj, type):
        self.obj = obj
        return self


class _BlockchainPartition(_PartitionDescriptor):
    """Non-data descriptor, provide access to blockchain api partition"
    """
    partition_url = '/blockchain'

    def __get__(self, obj, type):
        self.obj = obj
        return self

    def get_blockchain_info(self):
        u = self.partition_url + '/getBlockchainInfo'
        return self.obj._get_request(u)


class BitcoinCashABCClient(BaseCoinClient):
    """Provides access to bitcoin.com rest api

    api doc - https://rest.bitcoin.com/
    """

    base_url = 'https://rest.bitcoin.com/v2'

    blockchain = _BlockchainPartition()

    def get_median_time_past(self) -> int:
        info = self.blockchain.get_blockchain_info()
        try:
            info = json.loads(info)
        except json.JSONDecodeError as e:
            raise CoinClientUnexpectedException(
                'Error while json decode') from e

        key = 'mediantime'
        try:
            return int(info[key])
        except KeyError as e:
            # TODO: MTP can be calculated manually from block timestamps
            raise CoinClientUnexpectedException(
                'key %s not found in response, probably api changed' % (key, ))

    def _get_request(self,
                     url_path: str,
                     params: Union[Dict[str, str], List[Tuple[str, str]], str,
                                   None] = None) -> str:
        url = self.base_url + url_path
        try:
            req = requests.get(url, params)  # type: ignore
        except requests.exceptions.RequestException as e:
            raise CoinClientUnexpectedException('HTTP error') from e

        # TODO: add "status code not 200 OK" logic
        try:
            assert req.status_code == requests.codes.OK
        except AssertionError as e:
            raise CoinClientUnexpectedException(
                'Not 200 ok code on request') from e

        return req.text
