import random
import string
import tkinter as tk
from tkinter import messagebox

def gerar_senhas():
    try:
        tamanho = int(entry.get())
        if tamanho < 4:
            messagebox.showerror('Erro', 'Digite um número maior que 3!' )
            return
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        resultado.config(text=senha)
    except ValueError:
        messagebox.showerror('Erro', 'Digite um número valido!')

#Criar janelas
root = tk.Tk()
root.title('Gerador de senhas')
root.geometry('350x200')

#Campo de entrada
tk.Label(root, text='Digite o tamanho da senha: ').pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

#Botão para gerar
tk.Button(root, text='Gerar senhas', command=gerar_senhas).pack(pady=10)

#Onde a senha aparece
resultado = tk.Label(root, text='', font=('Arial', 12, 'bold'))
resultado.pack(pady=10)

#Rodar janela
root.mainloop()