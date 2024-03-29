import sys
import time

import pytest
from mock import Mock, patch

import hardfork


def test_hardfork_call_monitor():

    fake_argv = [None, '42']
    with patch('hardfork.tracker.monitor') as mock_monitor,\
        patch('sys.argv', fake_argv):
        from hardfork.__main__ import main
        main()
        mock_monitor.assert_called_once()


def test_hardfork_monitor_output(capfd):
    ts = 42
    MockCoinClient = Mock()
    MockCoinClient.get_median_time_past.return_value = ts
    hardfork.tracker.monitor(MockCoinClient, ts)

    out, _ = capfd.readouterr()
    s = 'hardfork'
    assert out.strip('\n').split('\n')[-1] == s


def test_hardfork_monitor(capfd):
    ts = 42
    MockCoinClient = Mock()
    MockCoinClient.get_median_time_past.side_effect = [ts - 2, ts - 1, ts]

    hardfork.tracker.monitor(MockCoinClient, ts)

    # one for now_ts == ts - 2
    # one for now_ts == ts -1
    # and one for now_ts == ts
    assert MockCoinClient.get_median_time_past.call_count == 3
