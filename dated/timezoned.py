from .dated import datedtime
from . import timezone


class timezoned(datedtime):

    @classmethod
    def _new_datetime(cls, year=None, month=None, day=None, hour=None, minute=None, second=None, microsecond=None,
                      tzinfo=None):

        if hour or minute or second or microsecond:
            assert tzinfo
        return super(timezoned, cls)._new_datetime(year, month, day, hour, minute, second, microsecond, tzinfo)


class local(timezoned):
    _timezone = timezone.local


class utc(timezoned):
    _timezone = timezone.utc

    def to_local(self):
        return self.astimezone(timezone.local)

