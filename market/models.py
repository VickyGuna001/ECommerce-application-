from market import db
from market import app
from market import bcrypt
from market import loginManager  # Renamed loginManager to login_manager
from flask_login import UserMixin

@loginManager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    mobile = db.Column(db.String(10), nullable=False)
    email_address = db.Column(db.String(50), nullable=False, unique=True)
    password_hashed = db.Column(db.String(60), nullable=False)
    items = db.relationship("Item", backref='owned_user', lazy=True)

    @property
    def password(self):
        return self.password_hashed

    @password.setter
    def password(self, plain_password):
        self.password_hashed = bcrypt.generate_password_hash(plain_password).decode('utf-8')

    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hashed, attempted_password)

with app.app_context():
    db.create_all()

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_url = db.Column(db.String(1020), nullable=False, unique=False)
    name = db.Column(db.String(50), nullable=False, unique=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    category = db.Column(db.String(25), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey(User.id))
    ratings = db.Column(db.Integer, nullable=False)
    opted = db.Column(db.Integer, nullable=False)
    reviews = db.relationship("Review", back_populates="item")

    def __repr__(self):
        return f'{self.name}'

class Review(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    reviewer_name = db.Column(db.String(255), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(Item.id), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    userReview = db.Column(db.Text, nullable=True)

    # Define a relationship with the Item table (not Reviews)
    item = db.relationship("Item", back_populates="reviews")

with app.app_context():
    db.create_all()
