Dated
=====

Enriches the datetime module with date string parsing (fuzzy and non-fuzzy) and time zone aware functions.

Two main modules: date times with time zone information and without.
In different occasions we need to convert back and forth from time zones without carrying a timezone (the tzinfo field
in a datetime object).
A classic example is storing timestamp in a ``sqlite`` databases where values should be stored in UTC and converted
to local timezone.

Examples
========
Without visible timezones

.. code-block:: python

    from dated import utc

    now_utc = utc.now()
    <class 'dated.notz.utc'>
    2014-06-19 21:22:47.007282
    assert not now_utc.tzinfo

    now_local = now_utc.to_local()
    <class 'dated.notz.local'>
    2014-06-19 22:22:47.007282

    utc_back = now_local.to_utc()
    <class 'dated.notz.utc'>
    2014-06-19 21:22:47.007282
    assert now_utc == utc_back

In reality the timezone information is there but is not visible

.. code-block:: python

    now_utc._timezone
    tzutc()

    now_local._timezone
    tzlocal()