from datetime import timedelta, datetime
from dateutil.tz import tzutc, tzlocal

utc = tzutc()
local = tzlocal()


class LocalOffset(tzlocal):
    def __init__(self, hours):
        super(LocalOffset, self).__init__()
        seconds = timedelta(hours=hours)
        self._dst_offset += seconds
        self._std_offset += seconds


def local_offset(hours):
    return LocalOffset(hours)


def convert_to_local_offset(date_time, plus):
    return date_time.replace(tzinfo=local).astimezone(LocalOffset(hours=plus))


def local_utc_offset():
    return local.utcoffset(datetime.now())