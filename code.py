import random
import string
import tkinter as tk
from tkinter import messagebox

def gerar_senha():
    try:
        tamanho = int(entry_tamanho.get())
        if tamanho < 4:
            messagebox.showwarning("Aviso", "O tamanho da senha deve ser pelo menos 4 caracteres.")
            return
        
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        entry_senha.delete(0, tk.END)
        entry_senha.insert(0, senha)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("400x200")
janela.resizable(False, False)

tk.Label(janela, text="Tamanho da senha:").pack(pady=5)
entry_tamanho = tk.Entry(janela)
entry_tamanho.pack(pady=5)

tk.Button(janela, text="Gerar Senha", command=gerar_senha).pack(pady=10)

tk.Label(janela, text="Senha Gerada:").pack(pady=5)
entry_senha = tk.Entry(janela, width=40)
entry_senha.pack(pady=5)

janela.mainloop()
