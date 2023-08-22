"""Server for movie ratings app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View homepage."""

    products = crud.get_products()

    return render_template("homepage.html", product_list=products)

@app.route("/login")
def login_page():
    """View login page"""

    return render_template("login.html")

@app.route("/loginprocess", methods=["POST"])
def login_process():
    """Process login user"""

    email = request.form.get("email")
    password = request.form.get("password")
    user = crud.get_user_by_email(email)

    if not user or user.password != password:
        flash("Email or password incorrect.")

        return redirect("/login")
    else:
        session["user_id"] = user.user_id
        session["profile_id"] = user.profile_id
        session["user_email"] = user.email
        flash(f"Welcome, {user.first_name}")

        return redirect("/")
    
@app.route("/registration")
def registration_page():
    """View registration page"""

    return render_template("registration.html")

@app.route("/registerprocess", methods=["POST"])
def register_process():
    """Register a new customer"""

    last_name = request.form.get("last_name")
    first_name = request.form.get("first_name")
    email = request.form.get("email")
    password = request.form.get("password")
    sex = request.form.get("sex")
    title = request.form.get("title")
    address = request.form.get("address")
    phone = request.form.get("phone")
    activity = request.form.get("activity")

    user = crud.get_user_by_email(email)

    # Check by email if user already exist
    if user:
        flash("Cannot create an account with that email. Try again.")

    # If user does'nt exist, create user
    else:
        profile = crud.get_profile_by_name("Customer")
        user = crud.create_user(profile, email, password, last_name, first_name, 
                    address, phone, activity, title, sex)
        
        db.session.add(user)
        db.session.commit()
        flash("Account created suscefful !")

    return redirect("/")

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
