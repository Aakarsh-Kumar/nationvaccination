import requests
import time
global URL, header
def findAvailability(pincode,date):
    URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(
        pincode,date)

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

    result = requests.get(URL, headers=header)
    if result.status_code==200:
        response_json = result.json()
        data = response_json["sessions"]
        return data
    else:
        return False