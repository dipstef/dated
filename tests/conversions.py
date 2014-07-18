from dated.notz import local as notz_local, utc as notz_utc
from dated.timezoned import local as tz_local, utc as tz_utc


def _tz_conversions_test(local, utc):
    local_now = local.now()
    utc_now = local_now.to_utc()

    assert utc_now == local_now.to_utc()
    assert local(utc_now) == local_now
    assert utc_now.to_local() == local_now
    assert local(local_now) == local_now
    assert utc(utc_now) == utc_now


if __name__ == '__main__':
    _tz_conversions_test(notz_local, notz_utc)
    _tz_conversions_test(tz_local, tz_utc)