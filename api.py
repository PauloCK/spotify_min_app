import json
import os

from flask import Flask, request, jsonify
from markupsafe import escape
from dotenv import load_dotenv
from bson import json_util

from db import insert_artist, get_all_artists

app = Flask(__name__)

load_dotenv()
print(os.getenv('MONGO_CONN'))


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/artists', methods=['GET','POST'])
def artists_handler():
    
    if request.method == 'POST':

        insert_artist(request.json['artist_name'])

        return 'OK'

    if request.method == 'GET':

        artist_list = get_all_artists()
        response = {'artists': json.dumps(artist_list,default=json_util.default)}
    
        return response


