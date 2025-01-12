#Personal system to practice coding in Python and to save my personal recepies

#System with friendly interface
#Funstions: add, edit, delete recipes
#Storage the recipes in a databank

import sqlite3;
import tkinter as tk;
from tkinter import ttk;

#BD connection and/or creation if non-existing

conn = sqlite3.connect('recipes.db')
cursosr = conn.cursor()

#Creation of a table with the desired info

cursor.execute('''CREATE TABLE IF NOT EXISTS recipes
                (id INTERGER PRIMARY KEY AUTOINCREMETN, 
                dish_name TEXT,
                origin TEXT,
                type TEXT,
                time_hours INTERGER,
                reference TEXT,
                rate INTERGER,
                ingredients TEXT,
                prepare TEXT)''')
conn.commit()
