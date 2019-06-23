import logging
import time
from datetime import datetime, timedelta

from .coinclients import BaseCoinClient


def monitor(coin_client: BaseCoinClient, timestamp: int):
    """\
    Monitors state of the blockchain, displays approximately  time to hardFork.
    On hardfork - print `hardfork`, then exit.
    """

    dt = datetime.fromtimestamp(timestamp + time.timezone)
    print('hardfork at %s (UTC+0)' % (dt))

    logging.debug('using %s client' % coin_client.__class__.__name__)

    while True:
        mtp = coin_client.get_median_time_past()
        if mtp >= timestamp:
            break

        time_now = datetime.now().strftime('%H:%M')
        # TODO: rewrite approximate delta calculation
        approximate_delta = timedelta(seconds=timestamp - mtp)
        print('[%s] approximately %s till hardfork' %
              (time_now, approximate_delta))
        # hardfork will happen in about `timestamp - mtp` seconds, but
        # since it is approximately, we divide by 2 to increase the accuracy
        sleep_time = (timestamp - mtp) // 2
        time.sleep(sleep_time)

    print('hardfork')
