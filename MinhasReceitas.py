#sistema pessoal para salvar minhas receitas

#sistema com interface amigável para usuário
#sistema com funcionalidades de adicionar, editar e excluir receitas
#armazenar receitas em um banco de dados

#tecnologias: Python - linguagem de programação e lógica de sistema,
#Tkinter: Python - library para criação de interfaces simples
#SQLite3: Python - banco de dados simples e leve integrado ao Python

import sqlite3;
import tkinter as tk;
from tkinter import ttk;



#Conexão ao BD e criação em caso de não existencia

conn = sqlite3.connect('receitas.db')
cursor = conn.cursor()

#criação de tabela - campos desejados

cursor.execute('''CREATE TABLE IF NOT EXISTS receitas
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               prato TEXT,
               origem TEXT,
               tipo TEXT,
               tempo_horas INTEGER,
               referencia TEXT,
               nota INTEGER,
               ingredientes TEXT,
               modo_preparo TEXT)''')
conn.commit()

#funções de interação com o banco de dados


def show_receitas():
    lista_receitas.delete(0, tk.END)
    cursor.execute("SELECT * FROM receitas")
    results = cursor.fetchall()
    receitas_ordenadas = sorted(results, key=lambda x: x[1])
    for receita in receitas_ordenadas:
        lista_receitas.insert(tk.END, f"{receita[1]}")

def initialize():
    show_receitas()

def add_receita():
    prato = enter_prato.get()
    origem = enter_origem.get()
    tipo = enter_tipo.get()
    tempo_horas = enter_tempo_horas.get()
    referencia = enter_referencia.get()
    nota = enter_nota.get()
    ingredientes = enter_ingredientes.get()
    modo_preparo = enter_modo_preparo.get()
    cursor.execute("INSERT INTO receitas (prato, origem, tipo, tempo_horas, referencia, nota, ingredientes, modo_preparo) VALUES (?,?,?,?,?,?,?,?)",
                   (prato, origem, tipo, tempo_horas, referencia, nota, ingredientes, modo_preparo))
    conn.commit()
    show_receitas()

def delete_receita():
    selected = lista_receitas.curselection()
    if selected:
        receita = lista_receitas.get(selected[0])

    cursor.execute("DELETE FROM receitas WHERE prato=?", (receita,))
    conn.commit()
    show_receitas()

def edit_receita():
    selected = lista_receitas.curselection()
    if selected:
        receita = lista_receitas.get(selected[0])
    cursor.execute("SELECT * FROM receitas WHERE prato=?", (receita,))
    result = cursor.fetchone()
    if result:
        enter_prato.delete(0, tk.END)
        enter_prato.insert(0, result[1])
        enter_origem.delete(0, tk.END)
        enter_origem.insert(0, result[2])
        enter_tipo.delete(0, tk.END)
        enter_tipo.insert(0, result[3])
        enter_tempo_horas.delete(0, tk.END)
        enter_tempo_horas.insert(0, result[4])
        enter_referencia.delete(0, tk.END)
        enter_referencia.insert(0, result[5])
        enter_nota.delete(0, tk.END)
        enter_nota.insert(0, result[6])
        enter_ingredientes.delete(0, tk.END)
        enter_ingredientes.insert(0, result[7])
        enter_modo_preparo.delete(0, tk.END)
        enter_modo_preparo.insert(0, result[8])
    cursor.execute("DELETE FROM receitas WHERE prato=?", (receita,))
    conn.commit()
    show_receitas()

def search_receitas():
    termo_pesquisa = search_prato.get()
    cursor.execute("SELECT * FROM receitas WHERE prato LIKE ?", ('%'+termo_pesquisa+'%',))
    results = cursor.fetchall()
    lista_receitas.delete(0, tk.END)
    for receita in results:
        lista_receitas.insert(tk.END, f"{receita[1]}")

#interface gráfica

window = tk.Tk()
window.title("Minhas Receitas")

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

#caixa de research
search_prato=ttk.Entry(frame_search, width=50)
search_prato.grid(row=0, column=0, padx=10)

btm_pesquisar = ttk.Button(frame_search, text="Pesquisar", command=search_receitas)
btm_pesquisar.grid(row=0, column=1, padx=10)

result_label = ttk.Label(frame, wraplength=300)
result_label.grid()

#btm_pesquisar = ttk.Button(frame, text="Pesquisar", command)

#campos para entrada de info

label_prato = tk.Label(frame, text="Nome do Prato: ",font=("Helvetica", 12, "italic"), fg="black", bg="#FFFAFA", padx=10, pady=15)
enter_prato = tk.Entry(frame, width=110)

label_prato.grid(row=1, column=0, sticky="w")
enter_prato.grid(row=1, column=1)

label_origem = tk.Label(frame, text= "Este prato é de origem: ", font=("Helvetica", 12, "italic"), fg="black",bg="#FFFAFA", padx=10, pady=15)
enter_origem = tk.Entry(frame, width=110)

label_origem.grid(row=2, column=0, sticky="w")
enter_origem.grid(row=2, column=1)

label_tipo = tk.Label(frame, text= "Qual tipo de prato: ", font=("Helvetica", 12, "italic"), fg="black", bg="#FFFAFA", padx=10, pady=15)
enter_tipo = tk.Entry(frame, width=110)

label_tipo.grid(row=3, column=0, sticky="w")
enter_tipo.grid(row=3, column=1)

label_tempo_horas = tk.Label(frame, text="Quantas horas de preparo total: ", font=("Helvetica", 12, "italic"), fg="black", bg="#FFFAFA", padx=10, pady=15)
enter_tempo_horas = tk.Entry(frame, width=110)

label_tempo_horas.grid(row=4, column=0, sticky="w")
enter_tempo_horas.grid(row=4, column=1)

label_referencia = tk.Label(frame, text="Página, Site ou Foto de referência: ", font=("Helvetica", 12, "italic"), fg="black", bg="#FFFAFA", padx=10, pady=15)
enter_referencia = tk.Entry(frame, width=110)

label_referencia.grid(row=5, column=0, sticky="w")
enter_referencia.grid(row=5, column=1)

label_nota = tk.Label(frame, text="De um total de 10, qual sua nota para esta receita? ", font=("Helvetica", 12, "italic"), fg="black", bg="#FFFAFA", padx=10, pady=15)
enter_nota = tk.Entry(frame, width=110)

label_nota.grid(row=6, column=0, sticky="w")
enter_nota.grid(row=6, column=1)

label_ingredientes = tk.Label(frame, text="Ingredientes: ", font=("Helvetica", 12, "italic"), fg="black", bg="#FFFAFA", padx=10, pady=15)
enter_ingredientes = tk.Entry(frame, width=110)

label_ingredientes.grid(row=7, column=0, sticky="w")
enter_ingredientes.grid(row=7, column=1)

label_modo_preparo = tk.Label(frame, text="Modo de Preparo: ", font=("Helvetica", 12, "italic"), fg="black", bg="#FFFAFA", padx=10, pady=15)
enter_modo_preparo = tk.Entry(frame, width=110,)

label_modo_preparo.grid(row=8, column=0, sticky="w")
enter_modo_preparo.grid(row=8, column=1)

#botões

add_button = tk.Button(frame_btm, text = "Add Receita", command=add_receita, fg="#7A2A2A", bg="#D1EAF5")
add_button.grid(row=10, column=0, sticky="s", padx=10, pady=30)

edit_button = tk.Button(frame_btm, text="Edit Receita", command=edit_receita, fg="#7A2A2A", bg="#D1EAF5")
edit_button.grid(row=10, column=2, sticky="s", padx=10, pady=30)

delete_button = tk.Button(frame_btm, text="Delete Receita", command=delete_receita, fg="#7A2A2A", bg="#D1EAF5")
delete_button.grid(row=10, column= 4, sticky="s", padx=10, pady=30)

#exibição da lista

lista_receitas = tk.Listbox(frame_lista, bg="#FFA39D", width=150, height= 5)
lista_receitas.grid(row=1, column=1,padx=20, pady=5)

def show_receita_detalhes(event):
    """Exibe os detalhes da receita selecionada."""
    index = lista_receitas.curselection()[0]
    nome_receita = lista_receitas.get(index)
    cursor.execute("SELECT * FROM receitas WHERE prato=?", (nome_receita,))
    resultado = cursor.fetchone()

    # Cria uma nova janela para exibir os detalhes
    detalhes_window = tk.Toplevel()
    detalhes_window.title(f"Detalhes da Receita: {nome_receita}")

    # Exibe os detalhes da receita em rótulos
    for i, valor in enumerate(resultado):
        tk.Label(detalhes_window, text=f"{list(cursor.description)[i][0]}: {valor}").grid()

# Associa o evento de clique à lista de receitas
lista_receitas.bind('<<ListboxSelect>>', show_receita_detalhes)
initialize()
window.mainloop()

conn.close()