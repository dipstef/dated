from datetime import datetime

_year_first = '%Y-%m-%d %H:%M:%S'
_year_after = '%d-%m-%Y %H:%M:%S'

_year_first_milli_sec = '%Y-%m-%d %H:%M:%S.%f'
_year_after_milli_sec = '%d-%m-%Y %H:%M:%S.%f'

_year_first_date = '%Y-%m-%d'
_year_after_date = '%d-%m-%Y'

_verbose_format = '%d %B %Y, %H:%M:%S'


def datetime_string(date_time, with_milliseconds=True):
    if with_milliseconds:
        return date_time.strftime(_year_first_milli_sec if date_time.microsecond else _year_first)
    else:
        return date_time.strftime(_year_first)


def date_string(date_time):
    return date_time.strftime(_year_first_date)


def datetime_verbose(date_time):
    return date_time.strftime(_verbose_format)


def datetime_from_string(date_str):
    try:
        return datetime.strptime(date_str, _year_first_milli_sec)
    except ValueError:
        return datetime.strptime(date_str, _year_first)


def date_from_string(date_str):
    return datetime.strptime(date_str, _year_first_date)