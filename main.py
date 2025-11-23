import requests

url = 'http://api.open-notify.org/iss-now.json'
response = requests.get(url)

# Convert response to JSON
data = response.json()
print(data)

# Raise error if request failed
response.raise_for_status()

# Extract coordinates
longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

location = (longitude, latitude)
print(location)
