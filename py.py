import sqlite3
while True:
    hello = int(input("Здравствуйте, желаете снять номер?"))
    if hello == 1:
        print("Отлично, выберите класс!")
    elif hello == 0:
        print("До свидания!")
        break
    else:
        print("Некорректный ввод. Пожалуйста, введите 1 для продолжения или 0 для выхода.")
while True:
    klass = int(input("Выберите класс\n1.Эконом\n2.Стандарт\n3.Делюкс"))
    break

cnct = sqlite3.connect('tickets.db')
crsr = cnct.cursor()
crsr.execute('''CREATE TABLE IF NOT EXISTS rooms (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    description TEXT,
                    price REAL,
                    availability TEXT
                )''')
crsr.execute("INSERT INTO rooms (name, description, price, availability) VALUES (?, ?, ?, ?)",
               ('Economy Room', 'Уютный стандартный номер c двуспальной кроватью', 50.00, '2024-04-15'))

crsr.execute("INSERT INTO rooms (name, description, price, availability) VALUES (?, ?, ?, ?)",
               ('Standard Room', 'Уютный стандартный номер c двуспальной кроватью', 100.00, '2024-04-15'))

crsr.execute("INSERT INTO rooms (name, description, price, availability) VALUES (?, ?, ?, ?)",
               ('Deluxe Suite', 'Просторный люкс c видом на море', 200.00, '2024-04-15, 2024-04-16'))

crsr.execute("SELECT * FROM rooms")
rows = crsr.fetchall()
for row in rows:
    print(row)

class Order: 
    def __init__(self, id, name, description, price, availability): 
        self.id = id 
        self.name = name 
        self.description = description 
        self.price = price 
        self.availability = availability 
     
         
class Check(Order): 
    def check(self): 
        check = f"select * from delivery" 
        print(check) 
    
         
class Add(Order): 
    def add(self): 
        add = f"insert into delivery values(1, 'Milk', 'A milk', 2000, 'Available')" 
        crsr.execute(add) 
        cnct.commit() 
      
         
class Delete(Order): 
    def delete(self): 
        delete = f"delete from delivery where id = 1" 
        crsr.execute(delete) 
        cnct.commit() 
         
 
class Update(Order): 
    def update(self): 
        update = f"update delivery set name = 'Apple' where id = 2" 
        crsr.execute(update) 
        cnct.commit()

cnct.commit()
cnct.close()
