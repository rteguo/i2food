"""Server for movie ratings app."""
import requests
from flask import Flask, render_template, request, flash, session, redirect, url_for, jsonify
from model import connect_to_db, db
import crud
import os
import json
from datetime import datetime
from jinja2 import StrictUndefined
from werkzeug.utils import secure_filename



now = datetime.utcnow
UPLOAD_FOLDER = 'static/img/product/'
DEFAULT_URL_IMAGE = '/static/img/product/default.jpg'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # Directory to store uploaded images
app.config['DEFAULT_URL_IMAGE'] = DEFAULT_URL_IMAGE # Set defaul url image for food 

@app.route("/")
def homepage():
    """View homepage."""

    user_name = None
    profile_id = None

    if "first_name" in session:
        user_name =  session["first_name"]

    if "profile_id" in session:
        profile_id = session["profile_id"]
    # Get the list of all products
    products = crud.get_products()

    return render_template("homepage.html", product_list=products, user_name = user_name, profile_id = profile_id)


@app.route("/about")
def about():
    """View About Us page"""
    user_name = None
    if "first_name" in session:
        user_name = session["first_name"]

    return render_template("about.html", user_name = user_name)


@app.route("/contact")
def contact():
    """View Contact page"""
    user_name = None
    if "first_name" in session:
        user_name = session["first_name"]

    return render_template("contact.html", user_name = user_name)


@app.route("/login")
def login_page():
    """View login page"""

    user_name = None

    if "first_name" in session:
        user_name =  session["first_name"]

    return render_template("login.html", user_name=user_name)


@app.route("/loginprocess", methods=["POST"])
def login_process():
    """Process login user"""

    email = request.form.get("email")
    password = request.form.get("password")
    user = crud.get_user_by_email(email)

    if not email or not password :
        return jsonify({"message" : "Please complete all required fields."})
    
    if not user or user.password != password:
        return jsonify({"message" : "Email or password incorrect."})
    
    else:
       
        session["user_id"] = user.user_id
        session["profile_id"] = user.profile_id
        session["email"] = user.email
        session["first_name"] = user.first_name

        #flash(f"Welcome, {user.first_name}")

        return jsonify({"message" : "Login successfully."})
    

@app.route("/registration")
def registration_page():
    """View registration page"""

    user_name = None

    if "first_name" in session:
        user_name =  session["first_name"]

    return render_template("registration.html", user_name = user_name)


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


@app.route("/product/<product_id>")
def product_details(product_id):
    """Show the details on a particular product."""

    user_name = None

    if "first_name" in session:
        user_name =  session["first_name"]

    product = crud.get_product_by_id(int(product_id))
    product_last_sale = crud.get_product_last_sale(int(product_id))

    # Set and send the API request
    query = product.name
    api_key = os.environ['TICKETMASTER_KEY']
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    data_api_dict = {}

    if response.status_code == requests.codes.ok:
        print(response.text)

        # Set the API data in a dictionary
        api_datas = response.json()
        print(api_datas)

        for data in api_datas:
            data_api_dict.update(data)
    else:
        print("Error:", response.status_code, response.text)
    
    products = crud.get_products()

    return render_template("product_details.html", product = product, response = data_api_dict, user_name=user_name, product_list = products, product_last_sale = product_last_sale)


@app.route("/shop")
def shoppage():
    """View shop page."""

    products = crud.get_products()
    categories = crud.get_categories()

    # Build dictionnary for the list of categories with number of products for each category
    dict_categories = {}

    for category in categories:
        dict_categories[category.name] = len(category.products)

    user_name = None

    if "first_name" in session:
        user_name =  session["first_name"]

    return render_template("shop.html", product_list=products, category_list=dict_categories, user_name = user_name)


@app.route("/logout")
def logout():
    """Remove the user from the session if is there"""

    # Reinitialize all the session variable
    session.pop("user_id", None)
    session.pop("profile_id", None)
    session.pop("email", None)
    session.pop("first_name", None)
    session.pop("cart", None)

    return redirect("/")


@app.route('/cart_size', methods=['GET'])
def get_cart_size():
    """Return the current cart size as JSON"""

    cart = session.get('cart', {})
    cart_size = len(cart)
    return jsonify(cart_size=cart_size)

@app.route("/cart")
def view_cart():
    """Diplay cart content"""

    # Keep track of the total cost of the order
    order_total = 0

    # Create a list to hold Food qobjects corresponding to the product_id's 
    # in the cart
    cart_products = []
    # Get the cart dictionary out of the session (or an empty one if none
    # exists yet)
    cart = session.get('cart', [])

    user_name = None
    
    if "first_name" in session:
        user_name =  session["first_name"]
    else:
        return render_template("login.html", user_name = user_name)

    # check if card is empty
    if cart:
        print(f" Taille dic = {len(cart)}")
        # Loop over the dictionnary
        for product_id, qty in cart.items():
            product = crud.get_product_by_id(product_id)

            # Calculate the total cost for this type of melon and add it to the
            total_cost = qty * product.price
            order_total += total_cost

            # Add the quantity and total cost as attributes on the Melon object
            product.qty = qty
            product.total_cost = total_cost

            # Add the Food object to our list
            cart_products.append(product)

    return render_template("cart.html", user_name=user_name, cart = cart_products, order_total = order_total)


@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    """Add food in the cart"""

    product_id = request.form.get('product_id')
    qty = int(request.form.get('qty'))
    product = crud.get_product_by_id(int(product_id))
    
    if product:
        #check if we already have products in the cart
        if "cart" in session:
            cart = session["cart"]
            
        else:
             # cart = session.setdefault("cart", {})
             cart = {}

        cart[product_id] = cart.get(product_id, 0) + qty 
        session["cart"] = cart

        return jsonify({"message": "Food added to cart successfully"})
    
    return jsonify({"message": "Food  not found"})

@app.route("/remove_from_cart", methods=["POST"])
def remove_from_cart():
    "Remove item from shopping cart"

    product_id = request.form.get("product_id")
    cart = session.get("cart", [])
    
    # check if shopping cart is empty
    if cart:
        cart.pop(product_id)
        session["cart"] = cart

        return jsonify({"message" : "Food removed from cart successfully"})
    
    else:

        return jsonify({"message" : "Shopping cart is empty"})


@app.route("/submit_order", methods=["POST"])
def submit_order():
    """Order submission the items in shopping cart"""

    cart = session.get("cart", [])
    order_total = float(request.form.get("order_total"))
    if cart:

        if "user_id" in session:

            today =  datetime.now()
            user = crud.get_user_by_id(int(session["user_id"]))
            state = "VA"
            order = crud.create_order(user, today, order_total, state)
            db.session.add(user)
            db.session.commit()
            
            for prod, qty in cart.items():

                product = crud.get_product_by_id(int(prod))
                
                # check the quantity of food ordered compared to the quantity available in stock
                if (qty > product.stock_qty):
        
                    return jsonify({"message" : "Overstock for" + product.name + " Food"})
                
                # Create each oder item
                order_item = crud.create_order_item(order, product, int(qty), float(qty*product.price))
                # Update the stock quantity
                product.stock_qty = product.stock_qty - qty
                db.session.add(order_item)
                db.session.add(product)
                db.session.commit()

            session.pop("cart", None)
            return jsonify({"message" : "Order sumit successfully"})
    
    else:

        return jsonify({"message" : "Shopping cart is empty"})

@app.route("/admin")
def admin_orders():
    """Display the list of orders in database"""

    # Check if login user and if he is an administrator
    user_name = None

    if "first_name" in session:
        user_name =  session["first_name"]
        if session["profile_id"] != 1 :
            return redirect("/")
    else:
        return redirect("/")
    

    # Get all the orders in data base
    orders = crud.get_orders()
    
    return render_template("admin.html", orders=orders, user_name = user_name)
                                       
@app.route("/adminproducts")
def admin_product():
    """Display the list of Food in database with all details"""

   # Check if login user and if he is an administrator
    user_name = None

    if "first_name" in session:
        user_name =  session["first_name"]
        if session["profile_id"] != 1 :
            return redirect("/")
    else:
        return redirect("/")
    
    products = crud.get_products_order_by_desc()
    
    return render_template("adminproducts.html", products=products, user_name = user_name)

@app.route("/addproduct")
def addproduct():
    """Form to add and update product"""

    # Check if login user and if he is an administrator
    user_name = None

    if "first_name" in session:
        user_name =  session["first_name"]
        if session["profile_id"] != 1 :
            return redirect("/")
    else:
        return redirect("/")

    # Get list of categories
    categories = crud.get_categories()
    
    return render_template("addproduct.html", categories=categories, user_name = user_name)

def allowed_file(filename):
    """check if an extension is valid before to upload the file"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/save_product", methods = ["POST"])
def save_product():
    "Save new product in database"

    name = request.form.get("name")
    category_id = request.form.get("category_id")
    description = request.form.get("description")
    price = request.form.get("price")
    rating = request.form.get("rating")
    stock_qty = request.form.get("stock_qty")
    unit_measure = request.form.get("unit_measure")
    image = request.files["image_url"]
    # file = request.form.get("image_url")
    print("================file========")
    print (image)

    if not name or not category_id or not price or not stock_qty:

        return jsonify({"message" : "Please complete all required fields"})
    
    else:
        category = crud.get_category_by_id(int(category_id))

        # Save the image and get the filename
        if image:

            if image.filename:
                #image_url = secure_filename(file.filename)
                image_url = app.config['UPLOAD_FOLDER'] + image.filename
                image.save(image_url)
                image_url = "/" + image_url
                # file.save(os.path.join(app.config['UPLOAD_FOLDER'], image_url))

        else:
            # Set defaut image
            image_url = app.config['DEFAULT_URL_IMAGE']
            return jsonify({"message" : "choose image"})
        
        product = crud.create_product(category, name, description, price, 
                    image_url, stock_qty, unit_measure, rating)

        db.session.add(product)
        db.session.commit()

        return jsonify({"message" : "Product added successfully"})

@app.route("/updateproduct/<product_id>")
def update_product_view(product_id):
    """Update the informations about a product."""

    # Check if login user and if he is an administrator
    user_name = None

    if "first_name" in session:
        user_name =  session["first_name"]
        if session["profile_id"] != 1 :
            return redirect("/")
    else:
        return redirect("/")

    product = crud.get_product_by_id(product_id)
    categories = crud.get_categories()

    return render_template("updateproduct.html", product = product, categories=categories, user_name=user_name)

@app.route("/update_product", methods = ["POST"])
def update_product():
    """Update existing product in database"""

    product_id = int(request.form.get("product_id"))
    name = request.form.get("name")
    category_id = int(request.form.get("category_id"))
    description = request.form.get("description")
    price = float(request.form.get("price"))
    rating = int(request.form.get("rating"))
    stock_qty = int(request.form.get("stock_qty"))
    unit_measure = request.form.get("unit_measure")
    image = request.files["image_url"]

    if not name or not category_id or not price or not stock_qty:

        return jsonify({"message" : "Please complete all required fields"})
    
    else:
        product = crud.get_product_by_id(product_id)
        product.name = name
        product.category_id = category_id
        product.description = description
        product.price = price
        product.rating = rating
        product.stock_qty = stock_qty
        product.unit_measure = unit_measure

        # Save the image and get the filename
        if image:

            if image.filename:
                #image_url = secure_filename(file.filename)
                image_url = app.config['UPLOAD_FOLDER'] + image.filename
                image.save(image_url)
                image_url = "/" + image_url
                # file.save(os.path.join(app.config['UPLOAD_FOLDER'], image_url))
                product.image_url = image_url

        db.session.add(product)
        db.session.commit()

        return jsonify({"message" : "Product updated successfully"})

@app.route("/admin/<order_id>")
def order_details(order_id):
    """Show the details on a particular product."""

    # Check if login user and if he is an administrator
    user_name = None

    if "first_name" in session:
        user_name =  session["first_name"]
        if session["profile_id"] != 1 :
            return redirect("/")
    else:
        return redirect("/")

    order_items = crud.get_order_items_by_order_id(order_id)
    order = crud.get_order_by_id(order_id)
    

    return render_template("order_details.html", order_items = order_items, order=order, user_name=user_name)

@app.route("/adminusers")
def admin_user():
    """Display the list of user in database with all details"""

   # Check if login user and if he is an administrator
    user_name = None

    if "first_name" in session:
        user_name =  session["first_name"]
        if session["profile_id"] != 1 :
            return redirect("/")
    else:
        return redirect("/")
    
    users = crud.get_users()
    
    return render_template("adminusers.html", users=users, user_name = user_name)

@app.route("/adduser")
def adduser():
    """Form to add new user"""

    # Check if login user and if he is an administrator
    user_name = None

    if "first_name" in session:
        user_name =  session["first_name"]
        # Check if user connected is administrator
        if session["profile_id"] != 1 :
            return redirect("/")
    else:
        return redirect("/")

    # Get list of categories
    profiles = crud.get_profiles()
    
    return render_template("adduser.html", profiles=profiles, user_name = user_name)

@app.route("/userprocess", methods=["POST"])
def register_user():
    """Register a new user"""

    last_name = request.form.get("last_name")
    first_name = request.form.get("first_name")
    email = request.form.get("email")
    password = request.form.get("password")
    sex = request.form.get("sex")
    title = request.form.get("title")
    address = request.form.get("address")
    phone = request.form.get("phone")
    activity = request.form.get("activity")
    profile_id = request.form.get("profile_id")

    user = crud.get_user_by_email(email)

    # Check by email if user already exist
    if user:
         return jsonify({"message" : "User already exist."})

    # If user does'nt exist, create user
    else:
        profile = crud.get_profile_by_id(profile_id)
        user = crud.create_user(profile, email, password, last_name, first_name, 
                    address, phone, activity, title, sex)
        
        db.session.add(user)
        db.session.commit()
        # flash("Account created suscefful !")

    return jsonify({"message" : "User crate successfully."})

@app.route("/contactprocess", methods=["POST"])
def contact_message():
    """Register a new user"""

    name = request.form.get("name")
    message = request.form.get("message")
    email = request.form.get("email")
   
    # Check if all required fields are complete
    if not name or not email:
        return jsonify({"message" : "Please complete all required fields"})

    else:
        contact = crud.create_contact(name, email, message)
        
        db.session.add(contact)
        db.session.commit()
        # flash("Account created suscefful !")

    return jsonify({"message" : "Conctact message create successfully."})

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
 