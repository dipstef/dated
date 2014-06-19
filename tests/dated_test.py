from datetime import timedelta

from dated import parser, date_from_string
from dated.timedelta import to_seconds


def _date_conversion_test(utc, local, must_have_timestamp=False):
    now_utc = utc.now()

    assert now_utc.tzinfo if must_have_timestamp else not now_utc.tzinfo
    now_local = utc.to_local(now_utc)

    assert now_local.tzinfo if must_have_timestamp else not now_local.tzinfo

    local_to_utc = local(now_local).to_utc()
    assert local_to_utc == now_utc


def _parse_date_test(utc, local, must_have_time_stamp=False):
    _str = str if not must_have_time_stamp else lambda v: v+' UTC'
    assert _str('01 March 2006, 07:42:00') == utc.from_string('01-03-2006, 07:42').verbose()
    assert '01 March 2006, 00:00:00' == utc.from_string('01-03-2006').verbose()

    assert _str('16 June 2013, 23:00:00') == local.from_string('17.06.2013, 00:00').to_utc().verbose()
    assert '17 June 2013, 00:00:00' == utc.from_string('17.06.2013').verbose()

    local_date = local.from_string('01.06.2013, 00:00')
    assert _str('31 May 2013, 23:00:00') == local_date.to_utc().verbose()
    assert '01 June 2013, 00:00:00' == utc.from_string('01.06.2013').verbose()

    assert _str('31 May 2013, 23:00:00') == local.from_string('2013.06.01, 00:00').to_utc().verbose()
    assert '01 June 2013, 00:00:00' == utc.from_string('2013.06.01').verbose()

    assert _str('16 June 2013, 23:00:00') == local.from_string('Jun 17, 2013, 00:00').to_utc().verbose()
    assert '17 June 2013, 00:00:00' == utc.from_string('Jun 17, 2013').verbose()

    assert '02 December 1985, 00:00:00' == utc.from_string('Dec. 2, 1985').verbose()
    assert '16 September 1990, 00:00:00' == utc.from_string('September. 16, 1990').verbose()
    assert '16 September 1990, 00:00:00' == utc.from_string('Sep. 16, 1990').verbose()
    try:
        assert not utc.from_string('Sept. 16, 1990').verbose()
    except ValueError:
        pass



def _fuzzy_date_string_test(module):
    now = module.now()

    parsed = module.from_fuzzy_string(u'6 hours ago, 5 minutes ago')

    sub = (now - timedelta(hours=6, minutes=5)).replace(microsecond=0)

    assert parsed == sub


def _date_strings_test(module):
    now = module.now()

    now_string = str(now)
    assert now == parser.parse_datetime(now_string)

    today_date = module.today()
    today_string = today_date.date_string()
    assert today_date == date_from_string(today_string)


def _run_tests(utc_module, local_module, must_have_timestamp=False):
    parsed_dt = local_module.from_string('01-03-2006, 00:00')
    parsed_d = local_module.from_string('01-03-2006')

    _date_conversion_test(utc_module, local_module, must_have_timestamp=must_have_timestamp)
    _parse_date_test(utc_module, local_module, must_have_time_stamp=must_have_timestamp)

    assert parsed_dt.date() == parsed_d.date()
    _fuzzy_date_string_test(utc_module)
    _fuzzy_date_string_test(local_module)

    _date_strings_test(utc_module)
    _date_strings_test(local_module)


def _time_delta_test():
    assert (2 * 60 * 60) + 2 * 60 == to_seconds(timedelta(hours=2, minutes=2))
    assert 10 * (24 * 60 * 60) + (2 * 60 * 60) + 2 * 60 == to_seconds(timedelta(days=10, hours=2, minutes=2))


def main():
    from dated.timezoned import timezoned_utc, timezoned_local
    from dated import notz

    _run_tests(notz.utc, notz.local)
    _run_tests(timezoned_utc, timezoned_local, must_have_timestamp=True)

    _time_delta_test()


if __name__ == '__main__':
    main()