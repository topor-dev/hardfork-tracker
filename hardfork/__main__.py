import argparse
import logging
import time
from datetime import datetime

from .coinclients import BitcoinCashABCClient
from .tracker import monitor


def _setup_logging(loglevel: int):
    logging.basicConfig(format='[%(asctime)s] %(levelname)s %(message)s',
                        level=loglevel)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog='hardfork')
    parser.add_argument(
        'timestamp',
        type=int,
        help='hardfork unix time or -1 (then current time will be used)')
    return parser.parse_args()


def main():
    args = _parse_args()

    if args.timestamp == -1:
        args.timestamp = int(time.time())
    assert args.timestamp > 0

    try:
        monitor(BitcoinCashABCClient(), args.timestamp)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    _setup_logging(logging.INFO)
    main()
