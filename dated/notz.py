from dated import datedtime, timezone


class no_timezone(datedtime):

    @classmethod
    def _new_datetime(cls, year=None, month=None, day=None, hour=None, minute=None, second=None, microsecond=None,
                           tzinfo=None):
        new_time = super(no_timezone, cls)._new_datetime(year, month, day, hour, minute, second, microsecond, None)
        new_time._timezone = tzinfo or cls._timezone
        return new_time

    def to_utc(self):
        return utc(super(no_timezone, self).to_utc())


class local(no_timezone):
    _timezone = timezone.local


class utc(no_timezone):
    _timezone = timezone.utc

    def to_local(self):
        return local(self.astimezone(timezone.local))

    @classmethod
    def _new_datetime(cls, year=None, month=None, day=None, hour=None, minute=None, second=None, microsecond=None,
                           tzinfo=None):
        new_time = super(no_timezone, cls)._new_datetime(year, month, day, hour, minute, second, microsecond, None)
        new_time._timezone = tzinfo or cls._timezone
        return new_time