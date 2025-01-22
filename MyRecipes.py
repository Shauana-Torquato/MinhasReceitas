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
  cursor.execute("DELETE FROM recipes WHERE dish_name=?", (recipe,))
  conn.commit()
  show_recipes()

def edit_recipes():
  select = recipes_list.curselection()
  if selected:
      recipe = recipes_list.get(selected[0])
  cursor.execute("SELECT * FROM recipes WHERE dish_name=?", (recipe,))
  result = cursor.fetchone()
  if result:
      enter_dish_name.delete(0, tk.END)
      enter_dish_name.insert(0, result[1])
      enter_origin.delete(0, tk.END)
      enter_origin.insert(0, result[2])
      enter_type.delete(0, tk.END)
      enter_type.insert(0, result[3])
      enter_time_hours.delete(0, tk.END)
      enter_time_hours.insert(0, result[4])
      enter_reference.delete(0, tk.END)
      enter_reference.insert(0, result[5])
      enter_rate.delete(0, tk.END)
      enter_rate.insert(0, result[6])
      enter_ingredients.delete(0, tk.END)
      enter_ingredients.insert(0, result[7])
      enter_preparation.delete(0, tk.END)
      enter_preparation.insert(0, result[8])
  cursor.execute("DELETE FROM recipes WHERE dish_name=?", (recipe,))
  conn.commit()
  show_recipes()

def search_recipes():
    word_research = search_dish_name.get()
    cursor.execute("SELECT * FROM recipes WHERE dish_name LIKE ?", ('%'+word_research+'%',))
    results = cursor.fetchall()
    list_recipes.delete(0, tk.END)
    for recipes in results:
      list_recipes.insert(tk.END, f"{recipe[1]}")
  
#graphic interface

window = tk.TK()
window.title("My Recipes")

window.configure(bg="#FFFAFA")

frame = tk.Frame(window)
frame.grid(sticky="nsew",padx=10, pady=10)
frame.configure(bg="#FFFAFA")

frame_search = tk.Frame(window)
frame_search.grid(sticky="nw",  padx=10, pady=10)
frame_search.configure(bg="#FFFAFA")

frame_btm = tk.Frame(window)
frame_btm.grid(sticky="sw", padx=10, pady=10)
frame_btm.configure(bg="#FFFAFA")

frame_lista = tk.Frame(window)
frame_lista.grid(sticky="nsew", padx=10, pady=10)
frame_lista.configure(bg="#FFFAFA")

#research box
search_dish_name=ttk.Entry(frame_search, width=50)
search_dish_name.grid(row=0, column=0, padx=10)

btm_search = ttk.Button(frame_search, text="Search", command=search_receitas)
btm_search.grid(row=0, column=1, padx=10)

result_label = ttk.Label(frame, wraplength=300)
result_label.grid()

