import sqlite3

# CRUD
# C - Create -> INSERT INTO ...
# R -> Retrive/Read -> select...FROM
# U - Update/Modify/Edit -> UPDATE ... SET ...
# D - Delete/Drop -> DELETE FROM ...

# step 1 : Import thesqlite3 module 
# step 2 : Create a database and a connection to the database
# step 3 : perfom sql stuff (CRUD) 

database = 'shop.db'

# Create a connection
connection = sqlite3.connect(database)

# function to create a table \
def create_table():
    # create table sql query(SQL STATEMENT)
    query = """CREATE TABLE IF NOT EXISTS product(
        product_id  INTERGER UNIQUE NOT NULL  PRIMARY KEY,          
        name char(20),
        quantity INTERGER,
        price REAL 
    ); 
    """
    # create a cursor object 
    cursor = connection.cursor()
    # user the cursor to execute the create table query 
    cursor.execute(query)
    # commit/save changes to the database DB
    connection.commit()
    # close the connection
    connection.close()
    

# perfom CRUD 
# create_table()

# 1. C- Create a product 
def create_product():
    #  create the insert query\
    query = "INSERT INTO product (product_id, name, quantity, price) VALUES (3, 'product - 3', 3, 20.50)"
    # create the cursor object 
    cursor = connection.cursor()
    # execute the query
    cursor.execute(query)
    # commit the changes
    connection.commit()
    # close the connection
    connection.close()
    
# create_product()

    
# 2. R - Read - view/Read one product
def read_one_product():
    # create query
    query = "SELECT * FROM product WHERE product_id = ?"
    # create cursor object
    cursor = connection.cursor()
    #  execute the query
    cursor.execute(query, [3])
    #fetch all products and store them in products variable 
    product = cursor.fetchone()
    # close the DB connection
    connection.close()
    # display the product
    print(f"{product[0]}. Name: {product[1]}, Quantity:{product[2]}, Price: {product[3]}")
    
# read_one_product()
# 2. R - Read - view/Read many product
def read_many_product():
    query = "SELECT * FROM product "
    # create cursor object
    cursor = connection.cursor()
    #  execute the query
    cursor.execute(query)
    #fetch all products and store them in products variable 
    products = cursor.fetchall()
    # close the DB connection
    connection.close()
    # read the product list
    # print(products)
    # display all the products 
    for products in products:
        print(f"{products[0]}, Name: {products[1]}, Quantity:{products[2]}, Price: {products[3]}")
        
    
# read_many_product()  
    
     
    

# 3. U - Update a product()
def update_product():
    # create the update query
    query = "UPDATE  product SET quantity = ? WHERE product_id = ? "
    # create cursor object
    cursor = connection.cursor()
    #  execute the query
    cursor.execute(query, [53, 3])
      # commit/save changes to the database DB
    connection.commit()
    # close the connection
    connection.close()
    
# update_product()

# 4. D - delete a product
def delete_one_product():
      # create the delete query
    query = "DELETE FROM   product WHERE product_id = ? "
    # create cursor object
    cursor = connection.cursor()
    #  execute the query
    cursor.execute(query, [3])
      # commit/save changes to the database DB
    connection.commit()
    # close the connection
    connection.close()

# delete_one_product()
# 4. D - Delete all products
def delete_all_products():
    # create query to delete all products 
    query = "DELETE  FROM product "
    # create cursor object
    cursor = connection.cursor()
    #  execute the query
    cursor.execute(query)
    # commit/save changes to the database DB
    connection.commit()
    # close the connection
    connection.close()

delete_all_products()
  
        
