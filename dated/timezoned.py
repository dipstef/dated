from .dated import datedtime
from . import timezone


class timezoned(datedtime):

    @classmethod
    def from_datetime(cls, dt):
        if not dt.tzinfo:
            try:
                dt = dt.replace(tzinfo=dt._timezone)
            except AttributeError:
                pass
        return super(timezoned, cls).from_datetime(dt)

    @classmethod
    def _new_datetime(cls, year=None, month=None, day=None, hour=None, minute=None, second=None, microsecond=None,
                      tzinfo=None):

        dt = super(timezoned, cls)._new_datetime(year, month, day, hour, minute, second, microsecond, tzinfo)
        if (hour or minute or second or microsecond) and not tzinfo:
            raise ValueError(str(dt) + ', must have timezone')
        return dt


class local(timezoned):
    _timezone = timezone.local

    def to_utc(self):
        return utc(super(local, self).to_utc())


class utc(timezoned):
    _timezone = timezone.utc

    def to_local(self):
        return local(self.astimezone(timezone.local))

