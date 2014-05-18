from .local_time import LocalTime
from .utc_time import UtcTime


class LocalTimeNormalized(LocalTime):

    def to_utc(self, date_time):
        utc_time = super(LocalTimeNormalized, self).to_utc(date_time)
        return utc_time.replace(tzinfo=None)

    def to_time_zone(self, date_time, timezone):
        converted = super(LocalTimeNormalized, self).to_time_zone(date_time, timezone)
        return converted.replace(tzinfo=None)


class UtcTimeNormalized(UtcTime):

    def now(self):
        now = super(UtcTimeNormalized, self).now()
        return now.replace(tzinfo=None)

    def to_time_zone(self, date_time, timezone):
        converted = super(UtcTimeNormalized, self).to_time_zone(date_time, timezone)
        return converted.replace(tzinfo=None)

local = LocalTimeNormalized()
utc = UtcTimeNormalized(local)