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
    return dated.from_datetime(value).to_string(format)


def date_string(value):
    return dated.from_datetime(value).date_string(format)


def date_from_string(value):
    return dated.from_string(value).midnight()


def datetime_date(value):
    return dated(value).midnight()


def today():
    now = dated.now()
    return now.midnight()


def is_midnight(dt):
    return dt.hour == 0 and dt.minute == 0 and dt.second == 0