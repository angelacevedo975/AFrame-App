from app import mongo
from flask import jsonify
from flask_pymongo import ObjectId
import datetime

def validate_user(user):
    users= mongo.db.Users.find_one( {"username": user} )
    if users:
        return False
    return True

def check_password(user, password):
    user_db= mongo.db.Users.find_one( {"username": user} )
    if user_db["password"] == password:
        return jsonify( {"status":200, "correct": True, "id": str( ObjectId(user_db["_id"]) ) } )
    return jsonify( {"status":200, "correct": False, "error": 2 } )


def add_user( user_dict ):
    try:
        mongo.db.Users.insert_one( user_dict )
        return True
    except:
        return False

def get_user(user_id):
    user= mongo.db.Users.find_one( {"_id": ObjectId(user_id) } )
    return user

def add_post( req ):
    user= get_user( req["_id"] )
    post= { "date": datetime.datetime.now(), "user": user["name"] +" "+ user["lastname"], "username": user["username"] ,"post": req["post"] }
    mongo.db.Posts.insert_one( post )

def get_posts( user_id ):
    posts= mongo.db.Posts.find( {  } )
    list_post=[]
    for post in posts:
        post["_id"] = str( ObjectId( post["_id"] ) )
        list_post.append( post )
    return list_post

