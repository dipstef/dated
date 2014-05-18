from distutils.core import setup

VERSION = '0.1'

desc = """Datetime handling, time-zone conversions and date string parsing (fuzzy and non-fuzzy).

The normalized module handles conversions between local and utc values without carrying time-zone information,
this is needed in situation like storing utc-timestamps in sqlite database
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