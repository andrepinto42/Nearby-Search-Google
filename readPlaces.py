import googlemaps
import pandas as pd
import json



def ReadData():
    f = open("Places.txt", "r")
    return f.readlines()

business_list = ReadData()
DataStruct = []


for business in business_list:
    print("hello")
    # DataStruct.append(json.loads(json.dumps(business)))
    # novito = json.loads(json.dumps(business))
    business= business.replace("'", '"')
    novito =json.load(business)
    print(novito)
    # print(novito["name"])
