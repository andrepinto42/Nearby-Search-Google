import googlemaps
import pandas as pd
import time
import sys



def GetNearbySearchNext(nextPageToken,locationI):
    return map_client.places_nearby(
    location=locationI,
    keyword=search_string,
    radius=distance,
    page_token = nextPageToken)

def GetNearbySearch(locationI):
    return map_client.places_nearby(
    location=locationI,
    keyword=search_string,
    radius=distance)

def WriteToFile(businessAll,f):
    for business in businessAll:
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

def SearchPlaces(locationI):
    next_page_token = "OK"
    while (next_page_token):
        if(next_page_token == "OK"):
            response = GetNearbySearch(locationI)
        else:
            response = GetNearbySearchNext(next_page_token,locationI)
    
        businessLog = response.get('results')

        print("Writing Restaurants...")
        WriteToFile(businessLog,f)

        next_page_token = response.get('next_page_token')
        time.sleep(2)




# --------INITIALIZATION---------------

API_KEY = 'AIzaSyDy5aM287nlSaU-m3wCIQ3rZNP9Ju40MuI'
map_client = googlemaps.Client(API_KEY)

# Location in latitude and longitude
locations = [     (41.560469, -8.396341)] #Universidade do Minho
locations.append( (41.550233, -8.429718)) # Arco da Sé de Braga
locations.append( (41.560948, -8.446355)) # Forno mágico de Braga
locations.append( (41.542109, -8.419280)) # Parque da Ponte
locations.append( (41.533292, -8.446146)) # Eleclerc Braga


# What you are searching for, or if you call this script with one argument with will use it
search_string = 'restaurant'
if (len(sys.argv) ==2) : search_string = str(sys.argv[1])

# Distance in meters
distance = 1000
# Filename output
outputName = "Places.txt"

business_list = []


# ("Name;Place_ID;Price_Level;Rating;UserRatings;Tags;Latitude|Longitude")
f = open(outputName, "w")

for locationI in locations:
    SearchPlaces(locationI)

f.close()
print("Script done writing to " + outputName + " using the keyword " + search_string)

