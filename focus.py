import requests

# Set up the API endpoint and parameters
url = 'https://www.googleapis.com/geolocation/v1/geolocate'
params = {'key': 'bf35fa512ce957745eb8759806283144'}

# Set up the WiFi access points
wifi_access_points = [
    {
        'macAddress': '00:11:22:33:44:55',
        'signalStrength': -70
    },
    {
        'macAddress': '66:77:88:99:AA:BB',
        'signalStrength': -80
    }
]

# Send a POST request to the API to retrieve the location data
response = requests.post(url, json={'wifiAccessPoints': wifi_access_points})
data = {'foo': 'bar'}

try:
    location = data['location']
except KeyError:
    location = None
    print(response.json())


print(location)  # prints "None"
# Parse the response to extract the latitude and longitude
location = response.json()['location']
latitude = location['lat']
longitude = location['lng']



# Print the latitude and longitude
print(f'Latitude: {latitude}, Longitude: {longitude}')
