from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


# init app

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init db
db = SQLAlchemy(app)
# init marshmallow
ma = Marshmallow(app)

# product class/model


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(100))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty


# Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')


# init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


# routes
@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'hello world'})

# create a product


@app.route('/products', methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']
    new_product = Product(name, description, price, qty)
    db.session.commit()
    return product_schema.jsonify(new_product)


# run server
if __name__ == '__main__':
    app.run(debug=True)