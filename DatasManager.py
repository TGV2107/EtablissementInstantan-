import csv
import sqlite3


def initDataBase(cursor):
    
    files = [("Users", "ID_user INT PRIMARY KEY, Name TEXT, Password TEXT, Type INT"),
             ("Classes","ID_user INT, ID_classe INT, FOREIGN KEY (ID_user) REFERENCES Users(ID_user)")]

    for file in files:
        name, rows = file

        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {name}({rows})''')

        with open("Datas/" + name + ".csv") as open_file:

            r = csv.reader(open_file)
            for row in r:
                args = ', '.join(['?' for _ in row])
                cursor.execute(f"INSERT INTO {name} VALUES ({args})", row)

def displayDatabase(cursor, table):
    
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()

    cursor.execute(f"PRAGMA table_info({table})")
    columns = [column[1] for column in cursor.fetchall()]

    print(", ".join(columns))

    for row in rows:
        print(", ".join(map(str, row)))