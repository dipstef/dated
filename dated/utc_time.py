from datetime import datetime
import time

from .date_parser import DateParser
from .time_zone import TimeZoneDateTime, local, utc


class UtcTime(TimeZoneDateTime, DateParser):

    def __init__(self, local_time):
        super(UtcTime, self).__init__(utc)
        self._local_time = local_time

    def now(self):
        return datetime.utcnow()

    def parse_datetime(self, date_string, day_first=True):
        if not 'utc' in date_string.lower():
            parsed = self._local_time.parse_datetime(date_string + ' UTC', day_first)
            if parsed and parsed.tzinfo:
                parsed = self._local_to_time_zone(parsed)
        else:
            parsed = self._local_time.parse_datetime(date_string, day_first)
            parsed = self._local_to_time_zone(parsed)
        return parsed

    def parse_datetime_fuzzy(self, fuzzy_str):
        parsed = self._local_time.parse_datetime_fuzzy(fuzzy_str)

        return self._local_to_time_zone(parsed)

    def _local_to_time_zone(self, parsed):
        return parsed and self._local_time.to_time_zone(parsed, self._timezone)

    def to_local(self, utc_time):
        return self.to_time_zone(utc_time, local)

    @staticmethod
    def from_timestamp(timestamp):
        date_time = datetime.utcfromtimestamp(time.mktime(timestamp))
        return date_time
