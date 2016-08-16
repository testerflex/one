import requests


base_url = "https://maps.googleapis.com/maps/api/geocode/json?"


def getting_users_input():
    user_address = raw_input('Enter location: ')
    while len(user_address) <= 1 or user_address.isdigit():
        user_address = raw_input('Enter correct location: ')
    return user_address


def return_location(user_address):
    try:
        response = requests.get(base_url, params=[('address', user_address)])
        if not response.status_code == 200:
            return "Error - Response: {}".format(response)
        js_obj = response.json()
        print js_obj['results'][0]['formatted_address']
    except requests.exceptons.RequestException as e:
        return "Error: {}".format(e)

print return_location(getting_users_input())