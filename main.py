import os
import sqlite3
import tkinter

import DatasManager as DM

#création de la base de donnée
connexion = sqlite3.connect('Datas/ESI.db')
cursor = connexion.cursor()

#Importation de la base de donnée depuis les csv

DM.initDataBase(cursor)
DM.displayDatabase(cursor,"Users")
DM.displayDatabase(cursor,"Classes")

window = tkinter.Tk()

label = tkinter.Label(window, text="Etablissement Scolaire Instantané")
label.pack()

window.mainloop()