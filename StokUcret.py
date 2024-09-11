from NesneTanima import nesne_tanima
from DatabaseConnecter import connect,product_finder

connect()
product_finder()

total_amount=0


sonuc=connect()
cursor=sonuc[0]
connection=sonuc[1]

alinanUrun=product_finder()
class_list = nesne_tanima()  
a=0







for i in alinanUrun:
    a+=1
    print(f"Ürün adı:{i[0]}\nÜrün fiyatı:{i[1]}\nÜrün stok:{i[2]-a}")
    
    print("////////////////////////////////////")
    total_amount+=int(i[1])
    
    
    urun_id = i[0]  
    cursor.execute("UPDATE products SET product_stock = product_stock - 1 WHERE product_name= %s", (urun_id,))  
    connection.commit()


    
    

    
    

print(f"Toplam tutar:{total_amount}")




