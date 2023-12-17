import sqlite3
conn = sqlite3.connect('noahs.sqlite')
c = conn.cursor()
clients = c.execute("""
                    SELECT customers.phone, customers.name, orders.ordered, products.sku, products.desc, customers.address
                    FROM customers 
                        JOIN orders ON customers.customerid = orders.customerid 
                        JOIN orders_items ON orders.orderid = orders_items.orderid 
                        JOIN products ON orders_items.sku = products.sku
                    WHERE products.desc LIKE '%Rug %'
                        AND customers.name LIKE 'J%P%'
                        AND orders.ordered BETWEEN '2017-01-01' AND '2017-12-31'
                    """).fetchall()
for client in clients:
    print(client)
