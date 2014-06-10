from dateutil import parser as date_parser
import parsedatetime as pdt
from .date_time import timetuple_to_datetime


_day_first = date_parser.parserinfo(dayfirst=True)


class DateParser(object):

    def parse_datetime(self, date_string, day_first=True):
        parser_info = _day_first if day_first else None

        parsed = date_parser.parse(date_string, fuzzy=True, parserinfo=parser_info)
        return parsed

    def parse_date(self, string_date, day_first=True):
        return self.parse_datetime(string_date, day_first=day_first).date()

    def parse_datetime_fuzzy(self, fuzzy_str):
        cal = pdt.Calendar()
        time_structure = cal.parse(fuzzy_str)

        return timetuple_to_datetime(time_structure[0]) if time_structure else None

    def parse_date_fuzzy(self, string_date):
        date_time = self.parse_datetime_fuzzy(string_date)
        return date_time.date() if date_time else None