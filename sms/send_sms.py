import requests

base_url = ["api.postcodes.io/postcodes/"]


def send_sms(postal_code):
    request_url = (base_url + '%s' + '?') % (postal_code)
    response = requests.get(request_url).json()
    if response['status'] == 200:
        return True
    else:
        return False
