from app import app, db
from flask import request, jsonify
from models import Friend

# CRUD applications
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

        required_fields = ["name", "role", "description", "gender"] # validating the fields
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f'Missing required field: {field}'}), 400

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


        new_freind = Friend(name=name, role=role, decription=description, gender=gender, img_url=img_url) 

        db.session.add(new_freind)
        db.session.commit()

        return jsonify({"msg": "friend created success"}), 201 # means some resource has been created
    
    except Exception as e:
        db.session.rollback() #what is rollback?
        return jsonify({"error": str(e)}), 500 # status code 500 is error
    
#delete ta friend

@app.route("/api/friends/<int:id>",methods=["DELETE"]) # ID type integer
def delete_friend(id):
    try:
        friend = Friend.query.get(id)
        if friend is None:
            return jsonify({"error": "Friend not found"}), 404
        
        db.session.delete(friend)
        db.session.commit()
        return jsonify({"msg": "Friend deleted"}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


#Update a friend profile

@app.route("/api/friends/<int:id>", methods=["PATCH"])
def update_friend(id):
    try:
        friend = Friend.query.get(id)
        if friend is None:
            return jsonify({"error": "Friend not found"}), 404
        
        data = request.json
        friend.name = data.get("name", friend.name) # if the user doesn't want to change the name default will be provided
        friend.role = data.get("role", friend.role) # if the user doesn't want to change the role default will be provided
        friend.description = data.get("description", friend.decription)  
        friend.gender = data.get("gender", friend.gender) 

        db.session.commit()
        return jsonify(friend.to_json()), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

