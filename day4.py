import sqlite3
conn = sqlite3.connect('noahs.sqlite')
c = conn.cursor()

clients = c.execute("""
                    SELECT COUNT(customers.name) AS visits, customers.phone, products.desc, orders.shipped, customers.name
                    FROM customers 
                        JOIN orders ON customers.customerid = orders.customerid
                        JOIN orders_items ON orders.orderid = orders_items.orderid
                        JOIN products ON orders_items.sku = products.sku
                    WHERE 
                        products.sku LIKE '%BKY%' 
                        AND CAST(strftime('%H', orders.shipped) AS INTEGER) < 5
                    GROUP BY customers.name
                    HAVING visits > 1
                    ORDER BY visits DESC
                    """).fetchall()
for c in clients:
    print(c)


