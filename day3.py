import sqlite3
conn = sqlite3.connect('noahs.sqlite')
c = conn.cursor()
clients = c.execute("""
                    SELECT customers.birthdate
                    FROM customers 
                    ORDER BY customers.birthdate DESC
                    LIMIT 1
                    """).fetchall()
print("Younger: ",clients[0][0])

clients = c.execute("""
                    SELECT customers.birthdate
                    FROM customers 
                    ORDER BY customers.birthdate ASC
                    LIMIT 1
                    """).fetchall()
print("Older: ", clients[0][0])

clients = c.execute("""
                    SELECT customers.birthdate, customers.name, customers.phone, products.desc, customers.address, orders.ordered
                    FROM customers 
                        JOIN orders ON customers.customerid = orders.customerid
                        JOIN orders_items ON orders.orderid = orders_items.orderid
                        JOIN products ON orders_items.sku = products.sku
                    
                    WHERE (customers.birthdate LIKE '%-06-%' AND CAST(strftime('%d', customers.birthdate) AS INTEGER) >= 22
                        OR customers.birthdate LIKE '%-07-%' AND CAST(strftime('%d', customers.birthdate) AS INTEGER) <= 22)
                        AND (customers.birthdate BETWEEN '1939-02-19' AND '1940-02-7' 
                        OR customers.birthdate BETWEEN '1951-02-6' AND '1952-01-26'
                        OR customers.birthdate BETWEEN '1963-01-25' AND '1964-02-12'
                        OR customers.birthdate BETWEEN '1975-02-11' AND '1976-01-30'
                        OR customers.birthdate BETWEEN '1987-01-29' AND '1988-02-16'
                        OR customers.birthdate BETWEEN '1999-02-16' AND '2000-02-04') 
                        AND products.desc LIKE '%Rug %'
                    GROUP BY customers.name
                    """).fetchall()
for c in clients:
    print(c)


