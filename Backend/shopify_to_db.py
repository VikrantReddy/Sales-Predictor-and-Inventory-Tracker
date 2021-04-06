import csv
from sqldb import sqldb
from models import Order,Order_Detail,Product
import random
from rich.progress import Progress 
import time

data = []

with open('Datasets/orders.csv') as file:
    reader = csv.DictReader(file)
    data = list(reader)

temp = {}

data = [dict(i) for i in data]

with Progress() as progress:
    products = {i["Lineitem sku"]:i["Lineitem name"] for i in data}
    task1 = progress.add_task("[cyan]Adding orders..",total=len(data))
    task2 = progress.add_task("[green]Adding products..",total=len(products))

    for row in data:
        if row["Financial Status"] == "paid":
            if len(temp) > 0:
                order = Order(temp)
                for detail in order.details:
                    if detail.product_sku.isnumeric():
                        sqldb.add_order_details(detail)
                        time.sleep(0.02)

            timestamp = row["Paid at"].split()
            temp = {
                "order_id":row["Name"][1:],
                "paid_at_time":timestamp[1],
                "paid_at_date":timestamp[0],
                "customer_name":row["Billing Name"],
                "items":[row["Lineitem sku"]]
            }
        else:
            temp["items"].append(row["Lineitem sku"])
        progress.update(task1,advance=1)

    for sku,name in products.items(): 
        if not sku.isnumeric():
            continue
        price = round(2.5 + random.normalvariate(5.0,1.5),2)
        product = Product(product_sku=sku,product_name=name,price=price)
        print(product.product_sku)
        sqldb.add_product(product)
        progress.update(task2,advance=1)

