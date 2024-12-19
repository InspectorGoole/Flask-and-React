from app import app, db
from flask import request, jsonify
from models import Friend

@app.route("/api/friends", methods=["GET"])
def get_freinds():
    friends = Friend.query.all() # select all from table friends
    result = [friend.to_json for friend in friends]
    return jsonify(result)