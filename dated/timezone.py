from datetime import timedelta, datetime
from dateutil.tz import tzutc, tzlocal
from pytz.reference import Central, Eastern, Mountain, Pacific

utc = tzutc()
local = tzlocal()


class LocalOffset(tzlocal):

    def __init__(self, hours):
        super(LocalOffset, self).__init__()
        hours_delta = timedelta(hours=hours)
        self._dst_offset += hours_delta
        self._std_offset += hours_delta


def local_offset(hours):
    return LocalOffset(hours)


def convert_to_local_offset(date_time, plus):
    return date_time.replace(tzinfo=local).astimezone(LocalOffset(hours=plus))


def local_utc_offset():
    return local.utcoffset(datetime.now())


def local_tz_str():
    return datetime.now(tz=local).strftime('%Z')


#conflicting timezone abbreviations:
#http://www.timeanddate.com/library/abbreviations/timezones/
#http://en.wikipedia.org/wiki/List_of_time_zone_abbreviations

_tz_str = '''-12 Y
-11 X NUT SST
-10 W CKT HAST HST TAHT TKT
-9 V AKST GAMT GIT HADT HNY
-8 U AKDT CIST HAY HNP PST PT
-7 T HAP HNR MST PDT
-6 S CST EAST GALT HAR HNC MDT
-5 R CDT COT EASST ECT EST ET HAC HNE PET
-4 Q AST BOT CLT COST EDT FKT GYT HAE HNA PYT
-3 P ADT ART BRT CLST FKST GFT HAA PMST PYST SRT UYT WGT
-2 O BRST FNT PMDT UYST WGST
-1 N AZOT CVT EGT
0 Z EGST GMT UTC WET WT
1 A CET DFT WAT WEDT WEST
2 B CAT CEDT CEST EET SAST WAST
3 C EAT EEDT EEST IDT MSK
4 D AMT AZT GET GST KUYT MSD MUT RET SAMT SCT
5 E AMST AQTT AZST HMT MAWT MVT PKT TFT TJT TMT UZT YEKT
6 F ALMT BIOT BTT IOT KGT NOVT OMST YEKST
7 G CXT DAVT HOVT ICT KRAT NOVST OMSST THA WIB
8 H ACT AWST BDT BNT CAST HKT IRKT KRAST MYT PHT SGT ULAT WITA WST
9 I AWDT IRKST JST KST PWT TLT WDT WIT YAKT
10 K AEST ChST PGT VLAT YAKST YAPT
11 L AEDT LHDT MAGT NCT PONT SBT VLAST VUT
12 M ANAST ANAT FJT GILT MAGST MHT NZST PETST PETT TVT WFT
13 FJST NZDT
11.5 NFT
10.5 ACDT LHST
9.5 ACST
6.5 CCT MMT
5.75 NPT
5.5 SLT
4.5 AFT IRDT
3.5 IRST
-2.5 HAT NDT
-3.5 HNT NST NT
-4.5 HLV VET
-9.5 MART MIT'''

#setting the default timezone abbreviation to the most popular ones:
# http://stackoverflow.com/questions/1703546/parsing-date-time-string-with-timezone-abbreviated-name-in-python


def __unsupported_abbreviations():
    tz_dict = {}
    import dateutil.parser as dp
    s = str(datetime.now())

    for tz_desc in map(str.split, _tz_str.split('\n')):
        tz_offset = int(float(tz_desc[0]) * 3600)
        for tz_code in tz_desc[1:]:
            try:
                tzinfo = dp.parse(s+' '+tz_code).tzinfo
            except:
                tzinfo = None
            if not tzinfo:
                tz_dict[tz_code] = tz_offset

    for us_tz in (Eastern, Central, Mountain, Pacific):
        if us_tz.stdname in tz_dict:
            tz_dict[us_tz.stdname] = us_tz
        if us_tz.dstname in tz_dict:
            tz_dict[us_tz.dstname] = us_tz
    return tz_dict

tz_abbreviations = __unsupported_abbreviations()
