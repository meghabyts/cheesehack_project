
import os
import random
from types import MethodDescriptorType

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/register", methods=["GET", "POST"])
def register():
     # Register via POST
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        #Check Confirmation Password
        elif not request.form.get("name"):
            return apology("must confirm password", 403)
            
        #Check adress
        elif not request.form.get("address"):
            return apology("must confirm password", 403)

        #Check city
        elif not request.form.get("city"):
            return apology("must confirm password", 403)

        #Check age
        elif not request.form.get("age"):
            return apology("must confirm password", 403)

        #Check major
        elif not request.form.get("major"):
            return apology("must confirm password", 403)

        #Check pronouns
        elif not request.form.get("pronouns"):
            return apology("must confirm password", 403)

        #Check location
        elif not request.form.get("location"):
            return apology("must confirm password", 403)

        #Check bio
        elif not request.form.get("bio"):
            return apology("must confirm password", 403)

         #Check genderpref
        elif not request.form.get("genderpref"):
            return apology("must confirm password", 403)

         #Check mess
        elif not request.form.get("mess"):
            return apology("must confirm password", 403)

        #Check sleep
        elif not request.form.get("sleep"):
            return apology("must confirm password", 403)
            
        #Check social
        elif not request.form.get("social"):
            return apology("must confirm password", 403)

        #Check if Passwords Match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords do not match", 403)

        #Get Username
        username = request.form.get("username")
        #Get Password
        password = generate_password_hash(request.form.get("password"))
        #Get Name
        name = request.form.get("name")
        #Get Address
        address = request.form.get("address")
        #Get City
        city = request.form.get("city")
        #Get Age
        age = request.form.get("age")
        #Get Major
        major = request.form.get("major")
        #Get Pronouns
        pronouns = request.form.get("pronouns")
        #Get Location
        location = request.form.get("location")
        #Get Bio
        bio = request.form.get("bio")
        #Get Genderpref
        genderpref = request.form.get("genderpref")
        #Get Mess
        mess = request.form.get("mess")
        #Get Sleep
        sleep = request.form.get("sleep")
        #Get Social
        social = request.form.get("social")
        
                
        #Generate Hash
        pwhash = password

        # Insert into database
        users = db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username=username, hash=pwhash, name=name, address=address, city=city, age=age, major=major, pronouns=pronouns, location=location, bio=bio, genderpref=genderpref, mess=mess, sleep=sleep, social=social)

        # Check if new username
        if not user:
            return apology("username is already registered")

        #remember
        session["user_id"]= user

        # Redirect user to login page
        return redirect("/login")

    # Register via GET
    else:
        # display reigstration form
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/match", methods=["GET", "POST"])
def match():
    username = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
    name = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("name"))
    age = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("age"))
    major = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("major"))
    bio = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("bio"))
    pref1 = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("genderpref"))
    pref2 = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("mess"))
    pref3 = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("sleep"))
    pref4 = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("social"))

    # mess levels, sleep times, social levels, gender pref
    userlist = [username, name, age, major, bio, pref1, pref2, pref3, pref4]
    score = 0

    op1 = random.randint(0, len(user_list))
    op2 = random.randint(0, len(user_list))
    # if op2 is the same as op1, change op2
    while (op2 == op1):
        op2 = random.randint(0, len(user_list))

    # op1
    username1 = userlist[0,op1]
    name1 = userlist[1,op1]
    age1 = userlist[2,op1]
    major1 = userlist[3,op1]
    bio1 = userlist[4,op1]
    pref1_1 = userlist[5,op1]
    pref2_1 = userlist[6,op1]
    pref3_1 = userlist[7,op1]
    pref4_1 = userlist[8,op1]
    # op2
    username2 = userlist[0,op2]
    name2 = userlist[1,op2]
    age2 = userlist[2,op2]
    major2 = userlist[3,op2]
    bio2 = userlist[4,op2]
    pref1_2 = userlist[5,op2]
    pref2_2 = userlist[6,op2]
    pref3_2 = userlist[7,op2]
    pref4_2 = userlist[8,op2]
    # match score calculation
    if (age1 == age2):
        score += 1
    if (major1 == major2):
        score += 1
    if (pref1_1 == pref1_2):
        score += 1
    if (pref2_1 == pref2_2):
        score += 1
    if (pref3_1 == pref3_2):
        score += 1
    if (pref4_1 == pref4_2):
        score += 1

    return ("TODO")
