import os

from flask import Flask, request
from markupsafe import escape
from dotenv import load_dotenv
app = Flask(__name__)

load_dotenv()
print(os.getenv('MONGO_CONN'))

@app.route('/')
def hello_world():
    return 'Hello, World!'

