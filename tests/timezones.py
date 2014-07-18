from datetime import datetime

from dateutil import parser as date_parser
from pytz.reference import Central

from dated import parser, utc


def test_abbreviated_timezones():
    dt_value = datetime(2014, 07, 15, 20, 23)
    utc_value = datetime(2014, 07, 16, 1, 23)

    datetime_string = u'Wed, 15 Jul 2014 20:23:00 CDT'

    parsed = date_parser.parse(datetime_string)
    assert parsed == dt_value
    assert not parsed.tzinfo

    parsed = parser.parse_datetime(datetime_string)
    assert parsed.tzinfo == Central
    parsed = parsed.replace(tzinfo=None)
    assert parsed == dt_value

    parsed = date_parser.parse(datetime_string, ignoretz=False, tzinfos={'CDT': Central})
    assert parsed.tzinfo == Central
    parsed = parsed.replace(tzinfo=None)
    assert parsed == dt_value

    parsed = date_parser.parse(datetime_string, ignoretz=False, tzinfos={'CDT': Central})
    assert utc(parsed) == utc_value

    parsed = utc.from_string(datetime_string)
    assert utc(parsed) == utc_value

if __name__ == '__main__':
    test_abbreviated_timezones()