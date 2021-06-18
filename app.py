import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, abort)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)



@app.route("/")
@app.route("/words")
def words():
    words = list(mongo.db.words.find())
    return render_template("words.html", words=words)



@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    words = list(mongo.db.words.find({"$text": {"$search": query}}))
    return render_template("words.html", words=words)    

#index by letter
@app.route("/alfabet/<letter>", methods=["GET"])
def search_by_letter(letter):
    regex = {"$regex": "^%s"  % letter}
    words = list(mongo.db.words.find({"Word": regex}))
    return render_template("words.html", words=words)  


#Register existing user

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")    

#Login existing user

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Username and/or password are not correct")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Username and/or password are not correct")
            return redirect(url_for("login"))

    return render_template("login.html")    


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))   

#Add new Word
@app.route("/add_word", methods=["GET", "POST"]) 
def add_word():
    if request.method == "POST":
        word = {
            "category_name": request.form.get("category_name"),
            "Word": request.form.get("Word"),
            "Meaning": request.form.get("Meaning"),
            "Link": request.form.get("Link"),
            "created_by": session["user"]
            }
        mongo.db.words.insert_one(word)
        flash("Word added Successfully")
        return redirect(url_for("add_word"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_word.html", categories=categories)


#Edit words
@app.route("/edit_word/<words_id>", methods=["GET", "POST"])
def edit_word(words_id):
    if request.method == "POST":
        word = {
            "category_name": request.form.get("category_name"),
            "Word": request.form.get("Word"),
            "Meaning": request.form.get("Meaning"),
            "Link": request.form.get("Link"),
            "created_by": session["user"]
            }
        mongo.db.words.update({"_id": ObjectId(words_id)}, word)
        flash("Word succesfully Updated")

    words = mongo.db.words.find_one({"_id": ObjectId(words_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_word.html", words=words, categories=categories)


#delete word
@app.route("/delete_word/<words_id>")
def delete_word(words_id):
    mongo.db.words.remove({"_id": ObjectId(words_id)})
    flash("Word succesfully Deleted")
    return redirect(url_for("words"))
        

#about 
@app.route("/about")
def about():

    return render_template("about.html")    



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)