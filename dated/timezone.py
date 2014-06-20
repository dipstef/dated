from datetime import timedelta, datetime
from dateutil.tz import tzutc, tzlocal

utc = tzutc()
local = tzlocal()


class LocalOffset(tzlocal):
    def __init__(self, hours):
        super(LocalOffset, self).__init__()
        hours_delta = timedelta(hours=hours)
        self._dst_offset += hours_delta
        self._std_offset += hours_delta


def local_offset(hours):
    return LocalOffset(hours)


def convert_to_local_offset(date_time, plus):
    return date_time.replace(tzinfo=local).astimezone(LocalOffset(hours=plus))


def local_utc_offset():
    return local.utcoffset(datetime.now())


def local_tz_str():
    return datetime.now(tz=local).strftime('%Z')