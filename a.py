import tkinter as tk
from tkinter import ttk

def mostrar_alternativa():
    alternativa_selecionada = combo.get()
    label_resultado.config(text=f"Alternativa selecionada: {alternativa_selecionada}")

# Criar janela principal
root = tk.Tk()
root.title("Campo de Texto com Alternativa")


# Criar combobox com alternativas
alternativas = ["Opção 1", "Opção 2", "Opção 3", "Opção 4", "Opção 5"]
combo = ttk.Combobox(root, values=alternativas)
combo.pack(pady=20)

# Botão para mostrar alternativa selecionada
btn_mostrar = tk.Button(root, text="Mostrar Alternativa", command=mostrar_alternativa)
btn_mostrar.pack()

# Label para exibir o resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=20)

# Rodar a aplicação
root.mainloop()
