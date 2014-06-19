from datetime import datetime
from . import timezone
from . import parser
from . import formatting


class datedtime(datetime):

    _timezone = timezone.local

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
        value._time_zone = value.tzinfo or cls._timezone
        return value

    @classmethod
    def now(cls, timezone=None):
        return cls(datetime.now(timezone or cls._timezone))

    @classmethod
    def today(cls):
        return cls.now().midnight()

    @classmethod
    def from_string(cls, value, day_first=True):
        tz_string = datetime.now(tz=cls._timezone).strftime('%Z')
        if not tz_string in value:
            value += ' ' + tz_string
        parsed = parser.parse_datetime(value, day_first=day_first)

        return cls.from_datetime(parsed)

    @classmethod
    def from_fuzzy_string(cls, value):
        fuzzy = parser.parse_datetime_fuzzy(value)
        fuzzy = fuzzy.replace(tzinfo=timezone.local)
        fuzzy = fuzzy.astimezone(cls._timezone)

        return cls.from_datetime(fuzzy)

    def to_string(self, format=formatting.default):
        return self.strftime(format).rstrip()

    def date_string(self):
        return self.to_string(format=formatting.date_default)

    def verbose(self):
        return self.to_string(format=formatting.verbose)

    def astimezone(self, timezone):
        to_timezone = self.replace(tzinfo=self._timezone)
        as_timezone = datetime.astimezone(to_timezone, tz=timezone)
        return self.from_datetime(as_timezone)

    def to_utc(self):
        return self.astimezone(timezone.utc)

    def midnight(self):
        return self.__class__(self.year, self.month, self.day)