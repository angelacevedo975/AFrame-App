from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo
import datetime
import sys


app= Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/bigApp"

mongo= PyMongo( app )


from controller import *

if __name__ == "__main__":
    app.run( debug=True )