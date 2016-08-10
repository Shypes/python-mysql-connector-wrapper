__author__ = 'oladayo'
import re, urllib, urlparse, uuid, requests
from random import randint
from math import floor
import time , datetime

class Utilities:
    @staticmethod
    def rand_string(length=15, chars='ABCDEFGHIJKLMNPQRSTUVWXYZabcdefghqrt123456789'):
        chars_length = (len(chars) - 1)
        string = chars[randint(0, chars_length)]
        for i in range(1, length):
            i = len(string)
            r = chars[randint(0, chars_length)]
            if r != string[i - 1]:
                string += r
        return string

    @staticmethod
    def generate_identity():
        user_id = uuid.uuid1().hex
        return user_id

    @staticmethod
    def msisdn_sanitizer(msisdn, plus=True):
        msisdn = str(msisdn).strip('')
        msisdn = msisdn.replace('+', '')
        if re.match('234', msisdn):
            msisdn = '0' + msisdn[3:]
        if len(msisdn) == 11:
            msisdn = '+234' + msisdn[1:]
        if not plus:
            msisdn = msisdn.replace('+', '')
        return msisdn

    @staticmethod
    def replace_message(message, params):
        return reduce(lambda text, replace_values: text.replace(*replace_values), params.iteritems(), message)

    @staticmethod
    def msisdn_extract(msisdn, plus=False):
        msisdn = str(msisdn).strip('')
        msisdn = msisdn.replace('+', '')
        if re.match('234', msisdn):
            msisdn = '0' + msisdn[3:]

        operator_code = msisdn[1:4]
        other_code = Utilities.rand_string(6, '0123456789')
        msisdn_extract = '+234' + operator_code + '1' + other_code
        if plus == False:
            msisdn_extract = msisdn_extract.replace('+', '')
        return msisdn_extract

    @staticmethod
    def url_generator(url, params):
        params = urllib.urlencode(params)
        if urlparse.urlparse(url)[4]:
            return url + '&' + params
        else:
            return url + '?' + params

    @staticmethod
    def curl(url):
        headers = {'content-type': 'text/plain'}
        req = requests.get(url, headers=headers)
        return req

    @staticmethod
    def htmlspecialchars(text):
        return (
            text.replace("&", "&amp;").
            replace('"', "&quot;").
            replace("<", "&lt;").
            replace(">", "&gt;")
        )
    @staticmethod
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False
    @staticmethod
    def get_date_difference_from_now(time_sub, timestamp = True):
        time_now = int(time.time())
        if(timestamp == False) :
            time_sub = datetime.datetime.strptime(time_sub)
            #print and confirm here
            #time_sub = strtotime(time_sub)
        datediff = time_now - time_sub
        days = floor(datediff/(60*60*24))
        return days

    @staticmethod
    def get_time_key(m = '',d = '',y = '') :
        d = time.strftime("%d") if d == '' else d
        m = time.strftime("%m") if m == '' else m
        y = time.strftime("%Y") if y == '' else y
        y = int(y) ; m = int(m) ; d = int(d)
        try:
            dt = datetime.datetime(year=y, month=m, day=d)
            return int(time.mktime(dt.timetuple()))
        except Exception :
            return ''

    @staticmethod
    def get_day_time(m = '',d = '',y = '') :
        d = time.strftime("%d") if d == '' else d
        m = time.strftime("%m") if m == '' else m
        y = time.strftime("%Y") if y == '' else y
        y = int(y) ; m = int(m) ; d = int(d)
        dt = datetime.datetime(year=y, month=m, day=d)
        return int(time.mktime(dt.timetuple()))

    @staticmethod
    def get_month_time(m = '',y = '') :
        m = time.strftime("%m") if m == '' else m
        y = time.strftime("%Y") if y == '' else y
        dt = datetime.datetime.strptime(str(y)+'-'+str(m), '%Y-%m')
        return int(time.mktime(dt.timetuple()))

    @staticmethod
    def send_content(param):
        url = 'http://46.38.169.102:14268/cgi-bin/sendsms?username=terragonosaro&password=terragonosaro&smsc=ETI_CONTENT&from='+param['from']+'&to='+param['to']+'&text='.urllib.quote_plus(param['response'])
        return Utilities.curl(url)

    @staticmethod
    def send_message(param):
        url = 'http://46.38.169.102:14233/cgi-bin/sendsms?username=terragonosaro&password=terragonosaro&smsc=ETI_VAS&from='+param['from']+'&to='+param['to']+'&text='.urllib.quote_plus(param['response'])
        return Utilities.curl(url)