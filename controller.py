from app import app
from model import *
from flask import render_template, request, jsonify


@app.route("/home/new", methods=["POST"])
def add_new_post():
    req= request.json
    add_post( req )
    return jsonify( {"status":200, "done": True} )

@app.route("/home/get", methods=["POST"])
def get_user_posts():
    req= request.json
    posts= get_posts( req["_id"] )
    return jsonify( { "status":200, "posts":posts } )


"""
     ERROR TYPES
     1: Not existent user
     2: Incorrect password
"""
@app.route("/login", methods=["POST"])
def validate_session():
    req= request.json
    if not validate_user( req["username"] ):
        correct= check_password( req["username"], req["password"] )

        return correct

    return jsonify( {"status": 200, "correct": False, "error": 1} )

@app.route("/register/validate", methods=["POST"])
def validate_register():
    try:
        req = request.json
        print(req)
        user = req["username"]

    except KeyError:
        return jsonify({"status": 400, "error": "Not enough data"})

    return jsonify({"status": 200, "free": validate_user(user)})


@app.route("/register", methods=["POST"])
def add_register():
    req = request.json
    try:
        user = {
            "name": req["name"],
            "lastname": req["lastname"],
            "username": req["username"],
            "password": req["password"]
        }
        #mongo.db.Users.insert_one( user )
        if add_user(user):
            return jsonify({"status": 200})
        else:
            return jsonify({"status": 400, "error": "Internal error"})

    except KeyError:
        return jsonify({"status": 400, "error": "Not enough data"})



@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")


@app.route("/home/<user_id>", methods=["GET"])
def home_user(user_id):
    return render_template("user.html", user= get_user(user_id) )

@app.route("/home/profile/<user_id>", methods=["GET"])
def profile(user_id):
    return render_template("profile.html", user= get_user(user_id) )
