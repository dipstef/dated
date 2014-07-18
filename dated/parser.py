from time import mktime
from dateutil import parser as date_parser
import parsedatetime as pdt
from datetime import datetime
from .timezone import tz_abbreviations

_day_first = date_parser.parserinfo(dayfirst=True)
cal = pdt.Calendar()


def parse_datetime(date_string, day_first=True, tz=tz_abbreviations, **kwargs):
    parser_info = _day_first if day_first else None

    parsed = date_parser.parse(date_string, fuzzy=True, parserinfo=parser_info, tzinfos=tz, **kwargs)
    return parsed


def parse_date(string_date, day_first=True, **kwargs):
    return parse_datetime(string_date, day_first=day_first, **kwargs).date()


def parse_datetime_fuzzy(fuzzy_str):
    time_structure = cal.parse(fuzzy_str)

    if time_structure:
        return datetime.fromtimestamp(mktime(time_structure[0]))


def parse_date_fuzzy(string_date):
    date_time = parse_datetime_fuzzy(string_date)
    return date_time.date() if date_time else None


