from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///friends.db"  #local database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # reduce the resources consumed, we dont care about the modifications flask makes

db = SQLAlchemy(app)

import routes

with app.app_context(): # for sqlalchemy
    db.create_all()
# creates the tables

if __name__ == "__main__": # this is needed bcuz when this file is imported or called by other files it will run all the contents automaically and we dont want that
    app.run(debug=True) # but this if statements makes sure that all the contents run only when the file is run directly

# Sometimes, the virtual environment's Scripts folder is not added to the PATH. Run the flask command directly: python -m flask run
# for powershell: .\venv\Scripts\activate
# for cmd: .\venv\Scripts\activate.bat
# the name of your env should be in green in the terminal