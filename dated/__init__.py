from . import formatting
from .dated import datedtime
from .notz import no_timezone, utc, local
from .timezoned import timezoned


class dated(datedtime):

    @classmethod
    def _new_datetime(cls, year=None, month=None, day=None, hour=None, minute=None, second=None, microsecond=None,
                      tzinfo=None):
        if tzinfo:
            return timezoned(year, month, day, hour, minute, second, microsecond, tzinfo)
        else:
            return no_timezone(year, month, day, hour, minute, second, microsecond)


def to_string(value, format=formatting.default):
    if format == formatting.default and is_midnight(value):
        return date_string(value)
    return datedtime.from_datetime(value).to_string(format)


def date_string(value):
    return datedtime.from_datetime(value).date_string(format)


def date_from_string(value):
    return datedtime.from_string(value).datetime()


def datetime_date(date_time):
    return datedtime(date_time).datetime()


def today():
    now = datedtime.now()
    return now.datetime()


def is_midnight(date_time):
    return date_time.hour == 0 and date_time.minute == 0 and date_time.second == 0