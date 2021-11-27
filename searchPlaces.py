import googlemaps
import pandas as pd
import time

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
# What you are searching for:
search_string = 'restaurant'
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
f.write("Name;Place_ID;Price_Level;Rating;UserRatings\n")

for business in business_list:     
    f.write(
    str(business.get('name')) + ';'
    + str(business.get('place_id')) + ';'
    + str(business.get('price_level')) + ';'
    + str(business.get('rating')) + ';'
    + str(business.get('user_ratings_total')) + "\n"
    )

f.close()
print("Script done writing to " + outputName)

