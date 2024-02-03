import pypyodbc

DRIVER_NAME = "SQL Server"
SERVER_NAME = "DESKTOP-O1BC0GF\SQLEXPRESS"
DATABASE_NAME = "test1"

try:
    connection_string = f"""
        DRIVER={{{DRIVER_NAME}}};
        SERVER={SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trusted_Connection=yes;
    """
    

    connection = pypyodbc.connect(connection_string, autocommit=True)
    db = connection.cursor()

    while True:
        
        Choice=int(input("choose the request :\n1-new user\n2-update your information\n3-search with National ID or Phone Number\n4-delete user\n5- do u want to exit?\nchoise num: "))
        
        if Choice == 1: 
            name = input("enter your name : ")
            age = int(input("enter your age : "))
            Nationality = input("enter your Nationality : ")
            phone = input("enter your cell phone numper : ")
            National_ID = input("enter National ID : ")
            values = (name, age, Nationality, phone,National_ID)
            query = "INSERT INTO users (name,age,nationality,phone,id) VALUES (?,?,?,?,?)"
            db.execute(query,values)
            
        if Choice == 2: 
            National_ID = input("enter your National ID : ")
            name = input("enter your new name or empty : ")
            age = input("enter your new age or empty : ")
            Nationality = input("enter your new nationality or empty : ")
            phone = input("enter your new cell phone numper or empty : ")
            attr = ""
            values = []
            if not name == "":
                attr += " name = ?,"
                values.append(name)
            if not age == "":
                attr += " age = ?,"
                values.append(age)
            if not Nationality == "":
                attr += " nationality = ?,"
                values.append(Nationality)
            if not phone == "":
                attr += " phone = ?,"
                values.append(phone)
            new_list = list(attr)
            attr = ""
            for letter in new_list[:-1]:
                attr += letter
            values.append(National_ID)
            query = f"UPDATE users SET{attr} WHERE id = ?"
            if len(values) > 1 :
                db.execute(query,values)
                print("updated successfully")

        if Choice == 3:
            id = input("enter your id :")
            query = "SELECT * FROM users WHERE id = ?"
            values = (id,)
            db.execute(query,values)


            print(db.fetchall())

        if Choice == 4:
            id = input("enter your id : ")
            query = "DELETE FROM users WHERE id = ?"
            values = (id,)

            db.execute(query,values)
            print("Data has been deleted")
        if Choice == 5:
            print("bye😝")
            break
except Exception as error:
    print("Couldn't connect to database")
    print(error)
finally:
    db.close()
    connection.close()




#varchar = نص
#primary kay = عدم التكرار

# -------------Create a Database
# db.execute("CREATE DATABASE test2")

# -------------Create a Table
    # query = "CREATE TABLE cars (name VARCHAR(50) PRIMARY KEY, color VARCHAR(15), price DECIMAL(10, 2))"
    # db.execute(query)

# -------------Delete a Table
    # db.execute("DROP TABLE cars")

# ---------------add a rowٍ
# query = "INSERT INTO cars (name, price, color) VALUES (?, ?, ?)"
# values = ('Toyota Corolla', 127250.25, 'white')
# db.execute(query, values)
# connection.commit()

# ---------------update a row
# query = "UPDATE cars SET color = ?, price = ? WHERE name = ?"
# values = ("red", 127000.50, "Toyota Corolla")
# db.execute(query, values)
# connection.commit()

# ---------------delete a row
# query = "DELETE FROM cars WHERE name = ?"
# values = ('Toyota Corolla',)
# db.execute(query, values)
# connection.commit()

# -----------Delete a column from the table
# query = "ALTER TABLE cars DROP COLUMN color"
# db.execute(query)
# connection.commit()

# -----------Delete a table
# query = "DROP TABLE cars"
# db.execute(query)
# connection.commit()
    
# ------------Get the data from the database
# query = "SELECT * FROM cars"
# db.execute(query)
# print(db.fetchall())