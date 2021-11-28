import googlemaps
import pandas as pd
import time
import sys



def GetNearbySearchNext(nextPageToken):
    return map_client.places_nearby(
    location=location,
    keyword=search_string,
    radius=distance,
    page_token = nextPageToken)

def GetNearbySearch():
    return map_client.places_nearby(
    location=location,
    keyword=search_string,
    radius=distance)

API_KEY = 'AIzaSyDy5aM287nlSaU-m3wCIQ3rZNP9Ju40MuI'
map_client = googlemaps.Client(API_KEY)

# Location in latitude and longitude
location = (41.56046969661545, -8.396341199436238)
# What you are searching for, or if you call this script with one argument with will use it
search_string = 'restaurant'
if (len(sys.argv) ==2) : search_string = str(sys.argv[1])

# Distance in meters
distance = 1000
# Filename output
outputName = "Places.txt"

business_list = []

response = GetNearbySearch()

business_list.extend(response.get('results'))

next_page_token = str(response.get('next_page_token'))

while next_page_token:
    time.sleep(2)
    response = GetNearbySearchNext(next_page_token)
    business_list.extend(response.get('results'))
    next_page_token = response.get('next_page_token')

f = open(outputName, "w")
f.write("Name;Place_ID;Price_Level;Rating;UserRatings;Tags;Latitude|Longitude\n")

for business in business_list:     
    # Caching the location
    locationBusiness = business.get('geometry').get('location')
    
    # Writes all tags in the format [bar,point_interest]
    allTags = '['
    tags = business.get('types')
    sT = len(tags)
    for i in range(sT -1):
        allTags += tags[i] + ','
    if (sT > 0):
        allTags += tags[sT-1]
    
    allTags += ']'
    
    f.write(
    str(business.get('name')) + ';'
    + str(business.get('place_id')) + ';'
    + str(business.get('price_level')) + ';'
    + str(business.get('rating')) + ';'
    + str(business.get('user_ratings_total'))  +';'
    + allTags +';'
    + str(locationBusiness.get('lat')) + '|' + str(locationBusiness.get('lng')) + "\n"
    )

f.close()
print("Script done writing to " + outputName + " using the keyword " + search_string)

