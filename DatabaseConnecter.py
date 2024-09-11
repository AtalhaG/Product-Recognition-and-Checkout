import mysql.connector 
from NesneTanima import nesne_tanima

connection = None
cursor = None

def connect():
    global connection, cursor
    connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345",
            database="product"
            
            )
    cursor= connection.cursor()
    print("Bağlantı başarılı")
    return cursor,connection



def product_finder():
    global  cursor

    class_list = nesne_tanima()  
    alinaUrun=[]
    for piece in class_list:
        
        
        
        cursor.execute(f"SELECT product_name,product_price,product_stock FROM products WHERE product_name='{piece}'")
        products=cursor.fetchall()
        
        for i in products:
            alinaUrun.append(i)
        
        
    return alinaUrun
    









