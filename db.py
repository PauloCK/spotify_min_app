import os

from pymongo import MongoClient

client = MongoClient(os.getenv('MONGO_CONN'))
db = client['spotify']
artists_collection = db['Artists']

def insert_artist(artist_name):

    to_insert = {'name': artist_name}
    artists_collection.insert(to_insert)
    

def get_all_artists():

    return list(artists_collection.find({}))


