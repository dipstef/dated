from datetime import timedelta

from dated.date_string import datetime_string, date_string, datetime_verbose, date_from_string, \
    datetime_from_string
from dated.date_time import today, to_seconds


def _date_conversion_test(utc, local, must_have_timestamp=False):
    now_utc = utc.now()

    assert now_utc.tzinfo if must_have_timestamp else not now_utc.tzinfo
    now_local = utc.to_local(now_utc)

    assert now_local.tzinfo if must_have_timestamp else not now_local.tzinfo

    assert local.to_utc(now_local) == now_utc


def _parse_date_test(utc):
    assert '01 March 2006, 07:42:00' == datetime_verbose(utc.parse_datetime('01-03-2006, 07:42'))
    assert '01 March 2006, 00:00:00' == datetime_verbose(utc.parse_datetime('01-03-2006'))

    assert '16 June 2013, 23:00:00' == datetime_verbose(utc.parse_datetime('17.06.2013, 00:00'))
    assert '17 June 2013, 00:00:00' == datetime_verbose(utc.parse_datetime('17.06.2013'))

    assert '31 May 2013, 23:00:00' == datetime_verbose(utc.parse_datetime('01.06.2013, 00:00'))
    assert '01 June 2013, 00:00:00' == datetime_verbose(utc.parse_datetime('01.06.2013'))

    assert '31 May 2013, 23:00:00' == datetime_verbose(utc.parse_datetime('2013.06.01, 00:00'))
    assert '01 June 2013, 00:00:00' == datetime_verbose(utc.parse_datetime('2013.06.01'))

    assert '16 June 2013, 23:00:00' == datetime_verbose(utc.parse_datetime('Jun 17, 2013, 00:00'))
    assert '17 June 2013, 00:00:00' == datetime_verbose(utc.parse_datetime('Jun 17, 2013'))

    assert '02 December 1985, 00:00:00' == datetime_verbose(utc.parse_datetime('Dec. 2, 1985'))
    assert '16 September 1990, 00:00:00' == datetime_verbose(utc.parse_datetime('September. 16, 1990'))
    assert '16 September 1990, 00:00:00' == datetime_verbose(utc.parse_datetime('Sep. 16, 1990'))
    assert _raises_error(lambda: datetime_verbose(utc.parse_datetime('Sept. 16, 1990')), ValueError)


def _raises_error(expression, error_class):
    try:
        expression()
        return False
    except error_class:
        return True
    except BaseException, e:
        return False


def _fuzzy_date_string_test(module):
    now = module.now()

    parsed = module.parse_datetime_fuzzy(u'6 hours ago, 5 minutes ago')

    sub = (now - timedelta(hours=6, minutes=5)).replace(microsecond=0)

    assert parsed == sub


def _date_strings_test(module):
    now = module.now()

    now_string = datetime_string(now)
    assert now == datetime_from_string(now_string)
    today_date = today()
    today_string = date_string(today_date)
    assert today_date == date_from_string(today_string)


def _run_tests(utc_module, local_module):
    parsed_dt = local_module.parse_datetime('01-03-2006, 00:00')
    parsed_d = local_module.parse_datetime('01-03-2006')

    _date_conversion_test(utc_module, local_module)
    _parse_date_test(utc_module)

    assert parsed_dt == parsed_d
    _fuzzy_date_string_test(utc_module)
    _fuzzy_date_string_test(local_module)

    _date_strings_test(utc_module)
    _date_strings_test(local_module)


def _time_delta_test():
    assert (2 * 60 * 60) + 2 * 60 == to_seconds(timedelta(hours=2, minutes=2))
    assert 10 * (24 * 60 * 60) + (2 * 60 * 60) + 2 * 60 == to_seconds(timedelta(days=10, hours=2, minutes=2))


def main():
    from dated import normalized
    import dated

    _run_tests(normalized.utc, normalized.local)
    #_run_tests(datelib.utc, datelib.local)

    _time_delta_test()


if __name__ == '__main__':
    main()