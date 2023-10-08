"""Models for movie ratings app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

now = datetime.utcnow

class Profile(db.Model):
    """A user profile."""

    __tablename__ = "profiles"

    profile_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    status = db.Column(db.Integer, default = 1)
    create_time = db.Column(db.DateTime, default=now)
    update_time = db.Column(db.DateTime, default=now, onupdate=now)

    users = db.relationship("User", back_populates = "profile")

    def __repr__(self):
        """Convenience method to show information about oject in console."""

        return f"Profile <profile_id={self.profile_id}> <name = {self.name}>"


class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey("profiles.profile_id"))
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String)
    last_name = db.Column(db.String)
    first_name = db.Column(db.String)
    address = db.Column(db.String)
    phone = db.Column(db.String)
    activity = db.Column(db.String)
    title = db.Column(db.String)
    sex = db.Column(db.String)
    status = db.Column(db.Integer, default = 1)
    create_time = db.Column(db.DateTime, default=now)
    update_time = db.Column(db.DateTime, default=now, onupdate=now)

    #ratings = db.relationship("Rating", back_populates="user")
    profile = db.relationship("Profile", back_populates="users")
    orders = db.relationship("Order", back_populates = "user")

    def __repr__(self):
        """Convenience method to show information about oject in console."""

        return f"<User user_id={self.user_id} email={self.email}>"


class Category(db.Model):
    """A category of product."""

    __tablename__ = "categories"

    category_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    weight = db.Column(db.Integer, default = 0)
    status = db.Column(db.Integer, default = 1)
    create_time = db.Column(db.DateTime, default=now)
    update_time = db.Column(db.DateTime, default=now, onupdate=now)

    products = db.relationship("Product", back_populates = "category")

    def __repr__(self):
        """Convenience method to show information about oject in console."""

        return f"Category <category_id={self.category_id}> <name = {self.name}>"


class Product(db.Model):
    """A product"""

    __tablename__ = "products"

    product_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.category_id"))
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    image_url = db.Column(db.String)
    stock_qty = db.Column(db.Integer)
    unit_measure = db.Column(db.String)
    rating = db.Column(db.Integer, default = 0)
    status = db.Column(db.Integer, default = 1)
    create_time = db.Column(db.DateTime, default=now)
    update_time = db.Column(db.DateTime, default=now, onupdate=now)

    category = db.relationship("Category", back_populates = "products")

    order_items = db.relationship("OrderItem", back_populates = "product")

    def __repr__(self):
        """Convenience method to show information about oject in console."""

        return f"Product <product_id = {self.product_id} name = {self.name}"
    
    def price_str(self):
        "Return price formatted as string $x.xx"

        return f"${self.price:.2f}"

class Order(db.Model):
    """A order of customer."""

    __tablename__ = "orders"

    order_id = db.Column(db.Integer, autoincrement = True, primary_key = True )
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable = False)
    order_date = db.Column(db.DateTime)
    total_amount = db.Column(db.Float)
    state = db.Column(db.String)
    status = db.Column(db.Integer, default = 1)
    create_time = db.Column(db.DateTime, default=now)
    update_time = db.Column(db.DateTime, default=now, onupdate=now)

    user = db.relationship("User", back_populates="orders")

    order_items = db.relationship("OrderItem", back_populates = "order")

    def __repr__(self):
        """Convenience method to show information about oject in console."""
        return f"Order <order_id = {self.order_id} user_id = {self.user_id}> "
    
    def total_amount_str(self):
        "Return total amount formatted as string $x.xx"

        return f"${self.total_amount:.2f}"
    
    def order_date_str(self):
        "Return order date formated"

        return self.order_date.isoformat(timespec='minutes')
    
class OrderItem(db.Model):
    """A order items."""

    __tablename__ = "order_items"

    order_item_id = db.Column(db.Integer, autoincrement = True, primary_key = True )
    order_id = db.Column(db.Integer, db.ForeignKey("orders.order_id"), nullable = False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.product_id"))
    quantity = db.Column(db.Integer)
    sub_total = db.Column(db.Float)
    status = db.Column(db.Integer, default = 1)
    create_time = db.Column(db.DateTime, default=now)
    update_time = db.Column(db.DateTime, default=now, onupdate=now)

    order = db.relationship("Order", back_populates="order_items")

    product = db.relationship("Product", back_populates = "order_items")

    def __repr__(self):
        """Convenience method to show information about oject in console."""
        
        return f"Order <order_item_id = {self.order_item_id} order_id = {self.order_id}> "

    def sub_total_str(self):
        "Return total amount formatted as string $x.xx"

        return f"${self.sub_total:.2f}"
    
class Contact(db.Model):
    """A contact message."""

    __tablename__ = "contacts"

    contact_id = db.Column(db.Integer, autoincrement = True, primary_key = True )
    name = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False)
    message = db.Column(db.Text, nullable = False)
    status = db.Column(db.Integer, default = 1)
    create_time = db.Column(db.DateTime, default=now)
    update_time = db.Column(db.DateTime, default=now, onupdate=now)

    def __repr__(self):
        """Convenience method to show information about oject in console."""
        
        return f"Contact <contact_id = {self.contact_id} name = {self.name}> "


def connect_to_db(flask_app, db_uri="postgresql:///i2food", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
