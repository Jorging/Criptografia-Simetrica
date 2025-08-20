import tkinter as tk
from tkinter import messagebox
import unicodedata
import string

# ----- Funções de limpeza de texto -----
def limpar_texto(texto):
    # Remove acentos
    texto = ''.join(
        c for c in unicodedata.normalize('NFKD', texto)
        if not unicodedata.combining(c)
    )
    # Mantém apenas letras e espaço
    permitido = string.ascii_letters + ' '
    return ''.join(c if c in permitido else '' for c in texto)

# ----- Funções de criptografia -----
def char_para_num(c):
    if c == " ":
        return 0
    return ord(c.lower()) - ord('a') + 1

def num_para_char(n):
    if n == 0:
        return " "
    return chr(n + ord('a') - 1)

def texto_para_numeros(texto):
    return [char_para_num(c) for c in texto]

def numeros_para_texto(nums):
    return "".join(num_para_char(n) for n in nums)

def repetir_chave(chave, tamanho):
    numeros_chave = texto_para_numeros(chave)
    return (numeros_chave * (tamanho // len(numeros_chave) + 1))[:tamanho]

def criptografar(mensagem, chave):
    msg = limpar_texto(mensagem)
    msg_nums = texto_para_numeros(msg)
    chave_nums = repetir_chave(chave, len(msg_nums))
    cript = [(m + k) % 27 for m, k in zip(msg_nums, chave_nums)]
    return numeros_para_texto(cript)

def descriptografar(mensagem, chave):
    msg_nums = texto_para_numeros(mensagem)
    chave_nums = repetir_chave(chave, len(msg_nums))
    decript = [(m - k) % 27 for m, k in zip(msg_nums, chave_nums)]
    return numeros_para_texto(decript)

# ----- Funções dos botões -----
def btn_criptografar():
    msg = entry_msg.get()
    chave = entry_chave.get()
    if not msg or not chave:
        messagebox.showwarning("Aviso", "Mensagem e chave são obrigatórias")
        return
    cript = criptografar(msg, chave)
    text_saida.delete(1.0, tk.END)
    text_saida.insert(tk.END, cript)

def btn_descriptografar():
    msg = entry_msg.get()
    chave = entry_chave.get()
    if not msg or not chave:
        messagebox.showwarning("Aviso", "Mensagem e chave são obrigatórias")
        return
    decript = descriptografar(msg, chave)
    text_saida.delete(1.0, tk.END)
    text_saida.insert(tk.END, decript)

# ----- GUI -----
root = tk.Tk()
root.title("Criptografia do Protagonista")
root.geometry("550x300")

# Frames
frame_entrada = tk.Frame(root, padx=10, pady=10)
frame_entrada.pack(fill="x")

frame_botoes = tk.Frame(root, pady=10)
frame_botoes.pack()

frame_saida = tk.Frame(root, padx=10, pady=10)
frame_saida.pack(fill="both", expand=True)

# Entradas
tk.Label(frame_entrada, text="Mensagem:", font=("Arial", 12)).grid(row=0, column=0, sticky="w")
entry_msg = tk.Entry(frame_entrada, width=40, font=("Arial", 12))
entry_msg.grid(row=0, column=1, pady=5)

tk.Label(frame_entrada, text="Chave:", font=("Arial", 12)).grid(row=1, column=0, sticky="w")
entry_chave = tk.Entry(frame_entrada, width=40, font=("Arial", 12))
entry_chave.grid(row=1, column=1, pady=5)

# Botões
btn_enc = tk.Button(frame_botoes, text="Criptografar", width=15, bg="#4CAF50", fg="white",
                    font=("Arial", 12), command=btn_criptografar)
btn_enc.grid(row=0, column=0, padx=10)

btn_dec = tk.Button(frame_botoes, text="Descriptografar", width=15, bg="#2196F3", fg="white",
                    font=("Arial", 12), command=btn_descriptografar)
btn_dec.grid(row=0, column=1, padx=10)

# Saída
text_saida = tk.Text(frame_saida, height=6, width=50, font=("Consolas", 12))
text_saida.pack()

root.mainloop()
