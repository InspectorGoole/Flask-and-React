from app import app, db
from flask import request, jsonify
from models import Friend

# get all friends
@app.route("/api/friends", methods=["GET"])
def get_freinds():
    friends = Friend.query.all() # select all from table friends
    result = [friend.to_json() for friend in friends]
    return jsonify(result)

#create a friend
@app.route("/api/friends", methods=["POST"])
def create_friend():
    try:
        data = request.json  # takw the request and convert to json
        name = data.get("name")
        role = data.get("role")
        description = data.get("description")
        gender = data.get("gender")

        # fetch avatar image based on gender
        if gender == "male":
            img_url = f"https://avatar.iran.liara.run/public/boy?username={name}"
        elif gender == "female":
            img_url = f"https://avatar.iran.liara.run/public/girl?username={name}"
        else:
            img_url = None


        new_freind = Friend(name=name, role=role, description=description, gender=gender, img_url=img_url) 

        db.session.add(new_freind)
        db.session.commit()

        return jsonify(new_freind.to_json()), 201 # means some resource has been created
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500 # status code 500 is error