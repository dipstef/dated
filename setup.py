from distutils.core import setup

VERSION = '0.1'

desc = """Misc date and time utilities, including conversion between local and utc timezone date-time values
and date-time string parsing (fuzzy and non-fuzzy).

The normalized module handles conversions between local and utc values, but does not carry time zone information,
this is particularly useful for situation like storing utc datetimes in a database as sqlite who does not support
time zones information and we need to convert back utc values to local.
"""

name = 'dated'

setup(name=name,
      version=VERSION,
      author='Stefano Dipierro',
      author_email='dipstef@github.com',
      url='http://github.com/dipstef/{}/'.format(name),
      description='Datetime handling and time-zone conversions functions',
      license='http://www.apache.org/licenses/LICENSE-2.0',
      packages=[name],
      platforms=['Any'],
      long_description=desc,
      requires=['dateutil', 'parsedatetime']
)