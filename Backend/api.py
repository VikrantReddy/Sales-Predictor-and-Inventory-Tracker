from flask import Flask,request,jsonify,render_template
from models import Order,Order_Detail,Product
from sqldb import sqldb
from flask_cors import CORS, cross_origin
from report import generate_report
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)
auth = HTTPBasicAuth()

users = {
    "vikrant": generate_password_hash("hello"),
    "nikhil": generate_password_hash("bye"),
    "trisanu": generate_password_hash("yo")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route("/")
@auth.login_required
def home():
    return render_template("index.html")


@app.route("/check_password")
def checkpass():
    return check_password_hash(users.get(username), password):

@app.route("/order/<int:order_id>", methods=["GET", "POST", "DELETE"])
def crud_order(order_id=None):
    if request.method == "POST":
        data = request.json(force=True)

        order = Order(data)

        sqldb.add_order(order)
        sqldb.add_order_details(order)

    elif request.method == "GET":
        sqldb.get_order(order_id)

    elif request.method == "DELETE":
        sqldb.delete_order(order_id)


@app.route("/order/bulk", methods=["POST", "DELETE"])
def bulk_order():
    if request.method == "POST":
        data_list = request.json(force=True)
        for data in data_list:
            order = Order(data)

            sqldb.add_order(order)
            sqldb.add_order_details(order)
    elif request.method == "DELETE":
        for data in data_list:
            sqldb.delete_order(data)


@app.route("/add_product", methods=["POST"])
def add_product():
    data = request.json(force=True)
    product = Product(data)
    sqldb.add_product(product)

@app.route("/get_order_data/<frequency>", methods=["GET"])
def get_products(frequency):
    return jsonify(sqldb.get_data_for_sales(frequency = frequency))

@app.route("/generate_report", methods=["GET"])
def get_report():
    return generate_report()

@app.route("/login",methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/signup",methods=["GET"])
def signup():
    return render_template("signup.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
