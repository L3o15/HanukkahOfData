import sqlite3
conn = sqlite3.connect('noahs.sqlite')
c = conn.cursor()
clients = c.execute('SELECT name, phone FROM customers').fetchall()

dict = {
    "A": "2",
    "B": "2",
    "C": "2",
    "D": "3",
    "E": "3",
    "F": "3",
    "G": "4",
    "H": "4",
    "I": "4",
    "J": "5",
    "K": "5",
    "L": "5",
    "M": "6",
    "N": "6",
    "O": "6",
    "P": "7",
    "Q": "7",
    "R": "7",
    "S": "7",
    "T": "8",
    "U": "8",
    "V": "8",
    "W": "9",
    "X": "9",
    "Y": "9",
    "Z": "9"
}

for client in clients:
    phone = client[1].replace('-', '')
    surname = client[0].split(' ')[1].upper()
    calculated_phone = ""
    for c in surname:
        calculated_phone += dict[c]
        #print(calculated_phone, phone)
        if len(calculated_phone) > len(phone):
            break
    if calculated_phone == phone:
        print(phone, client)
        break
        
    
    