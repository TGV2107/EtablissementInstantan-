import os
import sqlite3
import tkinter

import DatasManager as DM
from Window import *

#création de la base de donnée
connexion = sqlite3.connect('Datas/ESI.db')
cursor = connexion.cursor()

DM.initDataBase(cursor)
DM.printTable(cursor, "Users")
DM.table_exists(cursor, "Users")

#Importation de la base de donnée depuis les csv

main = Window("Main", "400x400", font=("Helevetica",35),bg=maincolor[0])
