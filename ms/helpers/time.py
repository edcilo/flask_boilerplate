import time
from datetime import datetime, timezone


def now():
    utc = timezone.utc
    return datetime.now(tz=utc)


def datetime_to_epoch(date):
    return int(date.timestamp())


def epoch_now():
    return int(time.time())
