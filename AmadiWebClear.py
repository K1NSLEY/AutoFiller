import tkinter as tk

# Função para quando os botões forem clicados
def button_click(btn_num):
    print(f"Botão {btn_num} clicado")

# Criação da janela principal
root = tk.Tk()
root.title("Interface com tkinter")
root.geometry("400x300")

# Adicionando os campos de texto
label1 = tk.Label(root, text="Campo de Texto 1")
label1.pack(pady=5)
entry1 = tk.Entry(root, width=50)
entry1.pack(pady=5)

label2 = tk.Label(root, text="Campo de Texto 2")
label2.pack(pady=5)
entry2 = tk.Entry(root, width=50)
entry2.pack(pady=5)

# Adicionando os botões
button1 = tk.Button(root, text="Botão 1", command=lambda: button_click(1))
button1.pack(side=tk.LEFT, padx=10, pady=20)

button2 = tk.Button(root, text="Botão 2", command=lambda: button_click(2))
button2.pack(side=tk.LEFT, padx=10, pady=20)

button3 = tk.Button(root, text="Botão 3", command=lambda: button_click(3))
button3.pack(side=tk.LEFT, padx=10, pady=20)

button4 = tk.Button(root, text="Botão 4", command=lambda: button_click(4))
button4.pack(side=tk.LEFT, padx=10, pady=20)

button5 = tk.Button(root, text="Botão 5", command=lambda: button_click(5))
button5.pack(side=tk.LEFT, padx=10, pady=20)

# Executando a janela principal
root.mainloop()
