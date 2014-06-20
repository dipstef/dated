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

    >>> now_utc = utc.now()
    "<class 'dated.notz.utc'>, 2014-06-19 21:22:47.007282"
    assert not now_utc.tzinfo

    >>> now_local = now_utc.to_local()
    "<class 'dated.notz.local'>, 2014-06-19 22:22:47.007282"

    >>> utc_back = now_local.to_utc()
    "<class 'dated.notz.utc'>, 2014-06-19 21:22:47.007282"
    assert now_utc == utc_back

In reality the timezone information is hidden

.. code-block:: python

    >>> now_utc._timezone
    'tzutc()'

    >>> now_local._timezone
    'tzlocal()'

Uses ``dateutil`` for non-fuzzy timestamp string parsing:

.. code-block:: python

    >>> local_parsed = local.from_string('2014-06-19 22:22:47.007282')
    assert local_parsed == now_local

    >>> local.verbose(with_millisec=True)
    '19 June 2014, 22:22:47.007282'

    assert local_parsed == local.from_string(local_parsed.verbose(with_millisec=True))

In British standard time:

.. code-block:: python

    local.from_string('2014.06.01, 00:00 UTC').verbose()
    '01 June 2014, 01:00:00'
    utc.from_string('2014.06.01, 00:00 UTC').verbose()
    '01 June 2014, 00:00:00'

    assert local.from_string('01 June 2014, 01:00:00 UTC') \
        == utc.from_string('01 June 2014, 01:00:00 UTC').to_local()


Uses ``parsedatetime`` for fuzzy timestamp string parsing:

.. code-block:: python

    >>> now_fuzzy = local.from_fuzzy_string('(3 days ago, 1 hour ago, 5 minutes ago')
    "<class 'dated.notz.local'>, '2014-06-16 21:22:42"


Offsets:

.. code-block:: python

    from dated.timezone import local_offset

    assert local_parsed.astimezone(local_offset(2)) == local_parsed + datetime.timedelta(hours=2)


With visible timezones, the string format includes timezone information

.. code-block:: python

    from dated.timezoned import utc, local
    from dated import timezone


    >>> tz_utc = utc(local_parsed.astimezone(tz=timezone.utc))
    "<class 'dated.timezoned.utc'>, 2014-06-19 21:22:47.007282+00:00"
    assert tz_utc.tzinfo is timezone.utc

    >>> tz_utc.verbose()
    '19 June 2014, 21:22:47 UTC'


    >>> tz_local = tz_utc.to_local()
    "<class 'dated.timezoned.local'>, 2014-06-19 22:22:47.007282+01:00"

    assert tz_local.tzinfo is timezone.local
    >>> tz_local.verbose()
    '19 June 2014, 22:22:47 BST'

    >>> timezone.local_tz_str()
    'BST'