from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Create app
app = Flask(__name__)
# Create SQL Extension
db = SQLAlchemy()
# Configure database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
# Initialize app with extension
db.init_app(app)

# Define Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String,unique=True,nullable=False)
    email = db.Column(db.String)
    
# Create table
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def username():
    Search = request.args.get("search")
    return render_template("search.html",search=Search)