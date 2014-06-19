from datetime import datetime
from . import timezone
from . import parser
from . import formatting


class datedtime(datetime):

    _time_zone = timezone.local

    def __new__(cls, *args):
        if len(args) == 1 and isinstance(args[0], datetime):
            return cls.from_datetime(args[0])
        else:
            return super(datedtime, cls).__new__(cls, *args)

    @classmethod
    def from_datetime(cls, dt):
        return cls._new_datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond, dt.tzinfo)

    @classmethod
    def _new_datetime(cls, year=None, month=None, day=None, hour=None, minute=None, second=None, microsecond=None,
                      tzinfo=None):
        value = super(datedtime, cls).__new__(cls, year, month, day, hour, minute, second, microsecond, tzinfo)
        value._time_zone = value.tzinfo or cls._time_zone
        return value

    @classmethod
    def now(cls, timezone=None):
        return cls(datetime.now(timezone or cls._time_zone))

    @classmethod
    def today(cls):
        return cls.now().datetime()

    @classmethod
    def from_string(cls, value, day_first=True):
        tz_string = datetime.now(tz=cls._time_zone).strftime('%Z')
        if not tz_string in value:
            value += ' ' + tz_string
        parsed = parser.parse_datetime(value, day_first=day_first)

        return cls.from_datetime(parsed)

    @classmethod
    def from_fuzzy_string(cls, value):
        fuzzy = parser.parse_datetime_fuzzy(value)
        fuzzy = fuzzy.replace(tzinfo=timezone.local)
        fuzzy = fuzzy.astimezone(cls._time_zone)

        return cls.from_datetime(fuzzy)

    def to_string(self, format=formatting.default):
        return self.strftime(format).rstrip()

    def date_string(self):
        return self.to_string(format=formatting.date_default)

    def verbose(self):
        return self.to_string(format=formatting.verbose)

    def astimezone(self, timezone):
        to_timezone = self.replace(tzinfo=self._time_zone)
        as_timezone = super(datedtime, to_timezone).astimezone(timezone)
        return self.from_datetime(as_timezone)

    def to_utc(self):
        return self.astimezone(timezone.utc)

    def datetime(self):
        return self.__class__(self.year, self.month, self.day)