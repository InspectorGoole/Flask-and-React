from app import db # model is just a table in our database

class Friend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    decription = db.Column(db.Text, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    img_url = db.Column(db.String(200), nullable=True)

    def to_json(self): #when u send data to client u want to send it in json type. Friend is going to be our usual argument
        return{
            "id":self.id,
            "name":self.name,
            "role":self.role,
            "decription":self.decription,
            "gender":self.gender,
            "imgUrl":self.img_url,

        }
