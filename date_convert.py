from datetime import datetime
from dateutil import tz
import sys

class DateConvert:

    def convert(self, utc_date):
        #utc_date = "9/26/18 11:59"

        ds = datetime.strptime(utc_date, '%m/%d/%y %H:%M')
        from_zone = tz.tzutc()
        to_zone = tz.tzlocal()

        utc = ds.replace(tzinfo=from_zone)
        central = utc.astimezone(to_zone)

        print("UTC TIME: {}".format(utc.strftime('%b %d %Y %I:%M%p')))
        print("CST TIME: {}".format(central.strftime('%b %d %Y %I:%M%p')))
        
if __name__ == '__main__':
    dc = DateConvert()
    print("Attempting to convert: {} {}".format(sys.argv[1], sys.argv[2]))
    indate = "{} {}".format(sys.argv[1], sys.argv[2])
    try:
        dc.convert(indate)
    except Exception as exp:
        print(exp)
        print("Error processing date {}.  Correct format is mm/dd/yy HH(24):MM\ne.g. python date_convert.py 9/26/18 11:59".format(sys.argv[1]))
