from datetime import datetime
from time import mktime


def today():
    now = datetime.now()
    return datetime_date(now)


def datetime_date(date_time):
    return datetime(date_time.year, date_time.month, date_time.day)


def is_midnight(date_time):
    return date_time.hour == 0 and date_time.minute == 0 and date_time.second == 0


def to_seconds(time_delta):
    seconds = time_delta.seconds
    seconds += 24 * 60 * 60 * time_delta.days
    return seconds


def exclude_milliseconds(date_time):
    return date_time.replace(microsecond=0)


def timetuple_to_datetime(time_tuple):
    return datetime.fromtimestamp(mktime(time_tuple))