import urllib.request
import json


while True:
    ip = input("Enter an IP address: ")
    url="http://ip-api.com/json/"
    response = urllib.request.urlopen(url+ip)
    values = json.loads(response.read())
    

    print("IP Address: ", values['query'])
    print("Country: ", values['country'])
    print("Region: ", values['regionName'])
    print("City: ", values['city'])
    print("ISP: ", values['isp'])
    print("Latitude: ", values['lat'])
    print("Longitude: ", values['lon'])
    print("Zip Code: ", values['zip'])
    print("Timezone: ", values['timezone'])
    print("Status: ", values['status'])
    
    
    latitude = values['lat']
    longitude = values['lon']
    google_maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"
    print("Google Maps Location: ", google_maps_url)
    
    break