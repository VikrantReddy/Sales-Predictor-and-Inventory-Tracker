import mysql.connector
import logging
import time
import random

is_local_test_instance = True

class wmysql():
    # wmysql(host='127.0.0.1', user='', passwd='', database='')
    def __init__(self, host=None, **kwargs):
        self.mydb = mysql.connector.connect(
            **kwargs,
            charset='utf8mb4',
            collation='utf8mb4_unicode_ci',
            use_unicode=True)

    def execute_tuple(self, sql, args):
        logging.info("Executing SQL: " + sql)
        self.mydb.start_transaction()
        c = self.mydb.cursor()
        c.execute(sql, args)
        if self.mydb.unread_result:
            res = c.fetchall()
        else:
            res = []
        self.mydb.commit()
        c.close()
        return res

    def execute_many(self, sql, args_list):
        logging.info("Executing many SQL: " + sql)
        self.mydb.start_transaction()
        c = self.mydb.cursor()
        c.executemany(sql, args_list)
        if self.mydb.unread_result:
            res = c.fetchall()
        else:
            res = []
        self.mydb.commit()
        c.close()
        return res

    def execute(self, sql, *args):
        return self.execute_tuple(sql, args)



class sql_queries():
    wsql = None
    allow_editing = False
    allow_deleting = False

    def __init__(self, allow_editing = False, allow_deleting = False):
        self.allow_editing = allow_editing
        if allow_editing:
            self.allow_deleting = allow_deleting
        else:
            self.allow_deleting = False

        self.wsql = wmysql(host='127.0.0.1', user='marketing', passwd='xIHG0MMZOe1pN7VGfQ47aV', database='reddit')

        if not self.allow_deleting:
            self.wsql.execute("SET SESSION sql_mode = 'STRICT_ALL_TABLES'")

        self.setup_tables()

    def declare_table(self, table_name, cols_list, extra_decl = []):
        args_str = ', '.join(cols_list + extra_decl)

        # Create SQL commands - NOTE - This is safe only because we are using constant strings
        # Don't have something stupid like input-defined table names
        rtable_sql = "CREATE TABLE IF NOT EXISTS {} ({}) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci".format(table_name, args_str)

        # Execute SQL
        self.wsql.execute(rtable_sql)


    def setup_tables(self):
        self.declare_table("orders", [
            "customer_name VARCHAR(50) NOT NULL"
            "order_id SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY",
            "paid_at_date VARCHAR(5) NOT NULL",
            "paid_at_time VARCHAR(5) NOT NULL",
        ])
        
        self.declare_table("order_details",[
            "order_detail_id SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY"
            "order_id SMALLINT NOT NULL",
            "product_sku MEDIUMINT NOT NULL",
        ])

        self.declare_table("products",[
            "product_sku MEDIUMINT NOT NULL PRIMARY KEY",
            "price TINYINT NOT NULL",
            "img_url TEXT CHARACTER SET latin1",
            "product_name TEXT CHARACTER SET latin1",
        ])

    def add_product(self):
        pass

    def add_order(self):
        pass

    def get_user_for_comment(self,trait):
        data = self.wsql.execute("SELECT username FROM account_traits WHERE username IS NOT NULL AND account_trait = %s",trait)
        
        if len(data):
            return data[0][random.randint(0,len(data)-1)]

if __name__ == "__main__":
    sqldb = sql_queries()
    # test = wmysql(host='127.0.0.1', user='fireice_test', passwd='fireice_test', database='reddit_test')
    #print(test.execute('describe comments'))
    #print(test.execute('select * from comments limit 10'))
    #print(test.execute('select * from comments where id = %s', 'fwe4wii'))
