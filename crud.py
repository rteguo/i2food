"""CRUD operations."""

from model import db, User, Product, Category, Profile, Order, OrderItem, connect_to_db


def create_user_login(email, password):
    """Create and return a new user with email and password."""

    user = User(email=email, password=password)

    return user

def create_user(profile, email, password, last_name, first_name, 
                address, phone, activity, title, sex):
    """Create and return user with all field"""

    user = User(profile=profile, email=email, password=password, 
                last_name=last_name, first_name=first_name, 
                address=address, phone=phone, activity=activity, 
                title=title, sex=sex) 
    return user

def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def create_profile(name, description):
    """Create and return user profile."""

    profile = Profile(name=name, description=description) 

    return profile

def get_profiles():
    """Return all profiles"""

    return Profile.query.all()

def get_profile_by_id(profile_id):
    """Return a profile by primary key"""

    return Profile.query.get(profile_id)

def get_profile_by_name(name):
    """Return a profile by name."""

    return Profile.query.filter(Profile.name == name).first()

def create_category(name, description, weight):
    """Create and return the category of product."""

    category = Category(name = name, description = description, weight = weight)

    return category

def get_categories():
    """Return all categories of product"""

    return Category.query.all()

def get_category_by_id(category_id):
    """Return category by primary key"""

    return Category.query.get(category_id)

def get_category_by_name(name):
    """Return  category by name."""

    return Category.query.filter(Category.name == name)

def create_product(category, name, description, price, 
                   image_url, stock_qty, unit_measure, rating ):
    """Create and return product."""

    product = Product(category = category, name = name, 
                      description = description, price = price, 
                      image_url = image_url, 
                      stock_qty = stock_qty, 
                      unit_measure = unit_measure, rating = rating)
    
    return product

def get_products():
    """Return all products"""

    return Product.query.all()

def get_product_by_id(product_id):
    """Return product by primary key."""

    return Product.query.get(product_id)

def get_product_by_name(name):
    """Return food by name"""

    return Product.query.filter(Product.name.ilike('%' + name + '%'))

def create_order(user, order_date, total_amount):
    """Create and return order"""

    order = Order(user = user, order_date = order_date, total_amount = total_amount)

    return order

def get_orders():
    """Return all the orders"""

    return Order.query.all()

def get_order_by_id(order_id):
    """Return order by primary key"""

    return Order.query.get(order_id)

def create_order_item(order, product, quantity, subtotal):
    """Create and return order item."""

    order_item = OrderItem(order = order, product = product, 
                           quantity = quantity, subtotal = subtotal)
    
    return order_item

def get_order_items():
    """Return all the order items."""

    return OrderItem.query.all()

def get_order_item_by_id(order_item_id):
    """Return order item by primary key"""

    return OrderItem.query.get(order_item_id)

if __name__ == "__main__":
    from server import app

    connect_to_db(app)
