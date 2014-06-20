import datetime
from dated import utc,local

now_utc = utc.now()
assert not now_utc.tzinfo
print now_utc
now_local = now_utc.to_local()
print type(now_local)
print now_local
utc_back = now_local.to_utc()
print type(utc_back)
print utc_back
assert now_utc == utc_back

local_parsed = local.from_string(str(now_local))
print local_parsed
assert local_parsed == now_local


local_parsed = local.from_string('2014-06-19 22:22:47.007282')
#assert local_parsed == now_local
print local_parsed.verbose(with_millisec=True)
verbose_parsed = local.from_string(local_parsed.verbose(with_millisec=True))
assert local_parsed == verbose_parsed


print local.from_string('2014.06.01, 00:00 UTC').verbose()

print utc.from_string('2014.06.01, 00:00 UTC').verbose()


assert local.from_string('01 June 2014, 01:00:00 UTC') \
    == utc.from_string('01 June 2014, 01:00:00 UTC').to_local()


now_fuzzy = local.from_fuzzy_string('(2 days ago, 1 hour ago, 5 minutes ago')
assert now_fuzzy == now_local.replace(microsecond=0) - datetime.timedelta(days=2, hours=1, minutes=5)

from dated.timezone import local_offset

assert local_parsed.astimezone(local_offset(2)) == local_parsed + datetime.timedelta(hours=2)


from dated.timezoned import utc, local
from dated import timezone

tz_utc = utc(local_parsed.astimezone(tz=timezone.utc))
print type(tz_utc)
assert tz_utc.tzinfo is timezone.utc
print tz_utc
print tz_utc.verbose()

tz_local = tz_utc.to_local()
print type(tz_local)
assert tz_local.tzinfo is timezone.local
print tz_local
print tz_local.verbose()