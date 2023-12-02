import os
import sqlite3
import tkinter

import DatasManager as DM
import Window as WM

#création de la base de donnée
connexion = sqlite3.connect('Datas/ESI.db')
cursor = connexion.cursor()

DM.initDataBase(cursor)
DM.printTable(cursor, "Users")
DM.table_exists(cursor, "Users")

#Importation de la base de donnée depuis les csv

window = tkinter.Tk()
window.minsize(800,500)
label = tkinter.Label(window, text="Etablissement Scolaire Instantané")
label.pack()

window.mainloop()