import requests
import json


base_url = "https://maps.googleapis.com/maps/api/geocode/json?"


# class TestGoogleMaps:

def function():
    user_address = raw_input('Enter location: ')
    while len(user_address) <= 1 or user_address.isdigit():
        user_address = raw_input('Enter correct location: ')


    a = requests.get(base_url, params=[('address', user_address)])
    print ('Retrieving', a.url)

    try:
        js = json.loads(a.content)
    except:
        js = None

    if 'status' not in js or js['status'] != 'OK':
        print('Failure')

    print json.dumps(js, indent=4)
    print js['results'][0]['formatted_address']


