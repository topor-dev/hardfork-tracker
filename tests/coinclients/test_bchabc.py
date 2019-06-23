import pytest
import requests
from mock import Mock, patch

from hardfork import coinclients


def test_get_request_handle_http_error():
    exc_to_raise = requests.exceptions.HTTPError('foo error')

    with patch('requests.get') as mocked_get:
        mocked_get.side_effect = exc_to_raise

        with pytest.raises(
                coinclients.CoinClientUnexpectedException) as actual_exc:

            bchabc = coinclients.BitcoinCashABCClient()
            bchabc.get_median_time_past()
        assert actual_exc.value.__cause__ == exc_to_raise


def test_get_requset_handle_json_decode_error():
    import json
    request_instance = Mock()
    request_instance.status_code = requests.codes.OK
    request_instance.text = '{invalid json'

    with patch('requests.get') as mocked_get:
        mocked_get.return_value = request_instance

        with pytest.raises(
                coinclients.CoinClientUnexpectedException) as actual_exc:

            bchabc = coinclients.BitcoinCashABCClient()
            bchabc.get_median_time_past()
        assert isinstance(actual_exc.value.__cause__, json.JSONDecodeError)
