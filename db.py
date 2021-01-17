import os

from dotenv import load_dotenv
from pymongo import MongoClient
load_dotenv()
client = MongoClient(os.getenv('MONGO_CONN'))

print(os.getenv('MONGO_CONN'))
# print('\n\n')
# print(client)

def insert_artist(artist_name):

    #myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['spotify']
    artists_collection = db['Artists']

    to_insert = [{'name': artist_name},{'name': 'Sticky Fingers'},{'name': 'Sons of the East'},{'name': 'Eminem'}]

    abelha = artists_collection.insert(to_insert)
    print(abelha)

insert_artist('Caetano Veloso')

