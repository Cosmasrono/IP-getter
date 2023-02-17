''' import requests
import folium

# Get the IP address to track from the user
ip_address = input("Enter an IP address to track: ")

# Make a request to the ipstack API to get the location data for the IP address
api_key = "<your-ipstack-api-key>"
url = f"http://api.ipstack.com/{ip_address}?access_key={api_key}"
response = requests.get(url)
data = response.json()

# Extract the latitude and longitude from the location data
latitude = data["latitude"]
longitude = data["longitude"]

# Create a map using folium and add a marker for the IP address location
map = folium.Map(location=[latitude, longitude], zoom_start=10)
folium.Marker(location=[latitude, longitude]).add_to(map)

# Save the map as an HTML file
map.save("map.html")
.html")
 '''
 
import requests

# Get your public IP address
ip_response = requests.get('https://api.ipify.org')
ip_address = ip_response.text

# Get your location data using the ipstack API
api_key = '16e19bc67099fb60de82429f777eeb57'
location_response = requests.get(f'http://api.ipstack.com/{ip_address}?access_key={api_key}')
location_data = location_response.json()

# Extract the relevant data from the location data
latitude = location_data['latitude']
longitude = location_data['longitude']
city = location_data['city']
region = location_data['region_name']
country = location_data['country_name']

# Print the results
print(f'Your IP address is: {ip_address}')
print(f'Your location is: {city}, {region}, {country} ({latitude}, {longitude})')
