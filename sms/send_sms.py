import requests


def send_sms(postal_code):
    request_url = ('api.postcodes.io/postcodes/' + postal_code)
    response = requests.get(request_url).json()
    if response['status'] == 200:
        return True
    else:
        return False
