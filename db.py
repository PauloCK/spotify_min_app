import os

from dotenv import load_dotenv
from pymongo import MongoClient
load_dotenv()
client = MongoClient(os.getenv('MONGO_CONN'))

db = client['spotify']
artists_collection = db['Artists']

print(os.getenv('MONGO_CONN'))
# print('\n\n')
# print(client)

def insert_artist(artist_name):

    #myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    to_insert = {'name': artist_name}

    artist = artists_collection.insert(to_insert)
    print(artist)

def get_all_artists():

    cursor = db['artists_collection'].find({})
    for item in cursor:
        print(item)

get_all_artists()

