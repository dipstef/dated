from datetime import datetime
from dated import timezone
from dated.dated import datedtime
from dated.notz import utc
from dated.timezoned import timezoned, timezoned_utc

utc_date = timezoned_utc.now()
assert utc_date.tzinfo == timezone.utc


datetime_now = datetime.now()
print datedtime(datetime_now)

print 'Utc Date: ', utc_date
timezoned_utc_now = timezoned(utc_date)
print 'Time zoned utc: ', timezoned_utc_now
print timezoned_utc_now
print timezoned_utc_now.astimezone(timezone.local)


print type(timezoned_utc_now.utcnow())

print 'Two days ago: ', utc.from_fuzzy_string('two days ago')
print 'Timezoned two days ago: ', timezoned_utc.from_fuzzy_string('two days ago')

#print datetime.now()
timezoned_utc_now_from_string = timezoned_utc.from_string(str(timezoned_utc_now))
print timezoned_utc_now_from_string
no_time_zone_utc_from_string = utc.from_string(str(timezoned_utc_now))
print no_time_zone_utc_from_string

assert timezoned_utc_now == timezoned_utc_now_from_string

print timezoned_utc_now_from_string
print timezoned_utc_now_from_string.to_string()

print timezoned_utc_now_from_string.verbose()
print no_time_zone_utc_from_string.verbose()
print no_time_zone_utc_from_string.to_string()