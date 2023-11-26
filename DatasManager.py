import csv
import sqlite3


def initDataBase(cursor : sqlite3.Cursor):
    """
    Params :
    - cursor : sqlite3.Cursor
    
    Returns :
    
    Fonction permettant d'innitialiser les tables non existantes dans la base de donnée"""
    
    #Liste des fichiers et de leurs clés
    files = [("Users", "ID_user INT PRIMARY KEY, Name TEXT, Password TEXT, Type INT"),
            ("Classes","ID_user INT, ID_classe INT, FOREIGN KEY (ID_user) REFERENCES Users(ID_user)")]

    for file in files:
        name, rows = file

        cursor.execute(f'''CREATE TABLE IF NOT EXISTS {name}({rows})''')

        #On ouvre le fichier csv correpondant
        with open("Datas/" + name + ".csv") as open_file:

            r = csv.reader(open_file)
            
            #On ajoute chaque ligne au fichier .db, en utilisant une chaîne de caractère contenant autant de ? que de paramètres devant aller dans la table
            for row in r:
                args = ', '.join(['?' for _ in row])
                cursor.execute(f"INSERT INTO {name} VALUES ({args})", row)

def printTable(cursor : sqlite3.Cursor, table : str):
    """
    Params:
    - cursor : sqlite3.Cursor()
    - table : str
    
    Returns :
    
    Fontion permettant d'afficher tous ce que contient la table passé en paramètre"""
    
    #Récupération des lignes de la table
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()

    #Affichage des colonnes
    cursor.execute(f"PRAGMA table_info({table})")
    columns = [column[1] for column in cursor.fetchall()]
    print(", ".join(columns))

    #Affichage des lignes
    for row in rows:
        print(", ".join(map(str, row)))

def table_exists(cursor : sqlite3.Cursor, table : str) -> bool:
    """
    Params :
    - cursor : sqlite3.Cursor()
    - table : str
    
    Returns :
    - bool
    
    Fonction renvoyant un booléen indiquant si la table existe dans la base de donnée du curseur"""

    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table'")
    return table in cursor.fetchone()