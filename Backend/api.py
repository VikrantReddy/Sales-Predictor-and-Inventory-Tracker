from flask import Flask,request
from models import Product,Order,Order_Detail
from sqldb import sqldb

app = Flask(__name__)

@app.route("/order/<order id>",methods=["GET","POST","DELETE"])
def add_order(order_id=None):
    if request.method == "POST":
        data = request.json(force=True)
        
        order = Order(data)
        order_details = Order_Detail(data)

        sqldb.add_order(order)
        sqldb.add_order_details(order)

    elif request.method == "GET":
        sqldb.get_order(order_id)
        
    elif request.method == "DELETE":
        sqldb.delete_order(order_id)

@app.route("/add_product",methods=["POST"])
def add_product():
    data = request.json(force=True)
    product = Product(data)
    sqldb.add_product(product)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
    