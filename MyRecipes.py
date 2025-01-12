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
                preparation TEXT)''')
conn.commit()

#interaction with the databank

def show_recipes():
  recipes_list.delete(0, tk.END)
  cursor.execute("SELECT * FROM recipes")
  results = cursor.fetchall()
  ordered_recipes = sorted (results, key = lambda x: x[1])
  for receipes in ordered_receipes:
      recipes_list.insert(tk.END, f"{recipe [1]}")

def initialize():
  show_recipes()

def add_recipes():
  dish_name = enter_dish_name.get()
  origin = enter_origin.get()
  type = enter_type.get()
  time_hours = enter_time_hours.get()
  reference = enter_reference.get()
  rate = enter_rate.get()
  ingredients = enter_ingredients.get()
  preparation = enter_preparation.get()
  cursor.execute("INSERT INTO recipes (dish_name, origin, type, time_hours, reference, rate, ingredients, preparation) VALUES (?,?,?,?,?,?,?,?)",
                  (dish_name, origin, type, time_hours, reference, rate, ingredients, preparation))
  conn.commit()
  show_recipes()

def delete_recipes():
  selected = recipes_list.curselection()
  if selected:
      recipe = recipes_list.get(selected[0])
  cursor.execute("DELETE FROM receitas WHERE dish_name=?", (recipe,))
  conn.commit()
  show_recipes()
