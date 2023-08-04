from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import os

# Create app
app = Flask(__name__)
# Create SQL Extension
db = SQLAlchemy()
# Configure database
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://user:pass@localhost/db_name'
# Initialize app with extension
db.init_app(app)

# Define Model 
class UserProfile(db.Model):
    __tablename__ = 'UserProfile'
    UserID = db.Column(db.String(20), primary_key=True)
    Username = db.Column(db.String(30), nullable=False)
    Email = db.Column(db.String(30), nullable=False)

class Recipe(db.Model):
    __tablename__ = 'Recipe'
    RecipeID = db.Column(db.String(20), primary_key=True)
    Title = db.Column(db.String(100))
    Country = db.Column(db.String(20), nullable=False)
    Limitation = db.Column(db.String(10), nullable=False)
    Difficulty = db.Column(db.Integer, nullable=False)
    UserRating = db.Column(db.Integer, nullable=False)
    Calories = db.Column(db.Integer, nullable=False)
    Tags = db.Column(db.String(100), nullable=False)
    CookTime = db.Column(db.Integer, nullable=False)
    UserID = db.Column(db.String(20), db.ForeignKey('UserProfile.UserID'), nullable=False)
    user_profile = db.relationship("UserProfile", back_populates="recipes")
    ratings = db.relationship("Rating", back_populates="recipe")

class Rating(db.Model):
    __tablename__ = 'Rating'
    RatingID = db.Column(db.String(30), primary_key=True)
    Comment = db.Column(db.String(250), nullable=False)
    Rating = db.Column(db.Integer, nullable=False)
    UserID = db.Column(db.String(20), db.ForeignKey('UserProfile.UserID'), nullable=False)
    RecipeID = db.Column(db.String(20), db.ForeignKey('Recipe.RecipeID'), nullable=False)
    user_profile = db.relationship("UserProfile", back_populates="ratings")
    recipe = db.relationship("Recipe", back_populates="ratings")
    
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

if __name__ == '__main__':
    app.run(debug=True)