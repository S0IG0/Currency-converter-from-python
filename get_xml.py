# import urllib.request
import grequests


def get_xml(year='2022', moth='04', day='22'):
    url = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={day}/{moth}/{year}'
    # response = urllib.request.urlopen(url)
    response, = grequests.map([grequests.get(url)])

    return response
