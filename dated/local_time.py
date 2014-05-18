from datetime import datetime
from .date_parser import DateParser
from .time_zone import TimeZoneDateTime, local, utc


class LocalTime(TimeZoneDateTime, DateParser):

    def __init__(self):
        super(LocalTime, self).__init__(local)

    @staticmethod
    def now():
        return datetime.now()

    def to_utc(self, date_time):
        return self.to_time_zone(date_time, utc)