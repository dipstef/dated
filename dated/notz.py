from . import datedtime, timezone


class no_timezone(datedtime):

    @classmethod
    def _new_datetime(cls, year=None, month=None, day=None, hour=None, minute=None, second=None, microsecond=None,
                           tzinfo=None):
        new_time = super(no_timezone, cls)._new_datetime(year, month, day, hour, minute, second, microsecond, None)
        new_time._timezone = tzinfo or cls._timezone
        return new_time

    def astimezone(self, tz):
        converted = self._convert_to(tz)
        if tz == timezone.utc:
            return utc(converted)
        elif tz == timezone.local:
            return local(converted)
        return no_timezone(converted)


class force_tz(no_timezone):

    @classmethod
    def from_datetime(cls, dt):
        tz = dt._timezone if isinstance(dt, datedtime) else dt.tzinfo
        if tz and tz != cls._timezone:
            dt = dt.astimezone(cls._timezone)
        return super(force_tz, cls).from_datetime(dt)


class local(force_tz):
    _timezone = timezone.local


class utc(force_tz):
    _timezone = timezone.utc