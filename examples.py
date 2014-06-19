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

print now_utc._timezone
print now_local._timezone

local_parsed = local.from_string(str(now_local))
print local_parsed
assert local_parsed == now_local

print
from datetime import datetime

from dated import timezone
from dated.dated import datedtime
from dated.timezoned import timezoned, utc


now_utc = utc.now()
print now_utc
assert now_utc.tzinfo == timezone.utc



datetime_now = datetime.now()
print datedtime(datetime_now)

print 'Utc Date: ', now_utc
timezoned_utc_now = timezoned(now_utc)
print 'Time zoned utc: ', timezoned_utc_now
print timezoned_utc_now
print timezoned_utc_now.astimezone(timezone.local)


print type(timezoned_utc_now.utcnow())

print 'Two days ago: ', utc.from_fuzzy_string('two days ago')
print 'Timezoned two days ago: ', utc.from_fuzzy_string('two days ago')

#print datetime.now()
timezoned_utc_now_from_string = utc.from_string(str(timezoned_utc_now))
print timezoned_utc_now_from_string
no_time_zone_utc_from_string = utc.from_string(str(timezoned_utc_now))
print no_time_zone_utc_from_string

assert timezoned_utc_now == timezoned_utc_now_from_string

print timezoned_utc_now_from_string
print timezoned_utc_now_from_string.to_string()

print timezoned_utc_now_from_string.verbose()
print no_time_zone_utc_from_string.verbose()
print no_time_zone_utc_from_string.to_string()