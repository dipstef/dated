from dated import datedtime, timezone


class no_timezone(datedtime):


    @classmethod
    def _new_datetime(cls, year=None, month=None, day=None, hour=None, minute=None, second=None, microsecond=None,
                           tzinfo=None):
        new_time = super(no_timezone, cls)._new_datetime(year, month, day, hour, minute, second, microsecond, None)
        new_time._time_zone = tzinfo or cls._time_zone
        return new_time


class local(no_timezone):
    _time_zone = timezone.local


class utc(no_timezone):
    _time_zone = timezone.utc

    def to_local(self):
        return self.astimezone(timezone.local)