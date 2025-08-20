import tkinter as tk
from tkinter import messagebox

def char_para_num(c):
    """Converte letra ou espaço em número (a=1..z=26, espaço=0)"""
    if c == " ":
        return 0
    return ord(c.lower()) - ord('a') + 1

def num_para_char(n):
    """Converte número (0..26) em letra ou espaço"""
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
    msg_nums = texto_para_numeros(mensagem)
    chave_nums = repetir_chave(chave, len(msg_nums))
    cript = [(m + k) % 27 for m, k in zip(msg_nums, chave_nums)]
    return numeros_para_texto(cript), msg_nums, chave_nums, cript

def descriptografar(mensagem, chave):
    msg_nums = texto_para_numeros(mensagem)
    chave_nums = repetir_chave(chave, len(msg_nums))
    decript = [(m - k) % 27 for m, k in zip(msg_nums, chave_nums)]
    return numeros_para_texto(decript)

# 🔑 Exemplo
mensagem = "vamos jogar hoje cara de lata"
chave = "roblox"

cript, msg_nums, chave_nums, cript_nums = criptografar(mensagem, chave)
print("Mensagem original:", mensagem)
print("Mensagem em números:", msg_nums)
print("Chave em números:   ", chave_nums)
print("Soma (mod 27):      ", cript_nums)
print("Mensagem criptografada:", cript)

decript = descriptografar(cript, chave)
print("Mensagem descriptografada:", decript)

def btn_criptografar():
    msg = entry_msg.get()
    chave = entry_chave.get()
    if not msg or not chave:
        messagebox.showwarning("Aviso", "Mensagem e chave são obrigatórias")
        return
    cript, _, _, _ = criptografar(msg, chave)
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
root.title("Criptografia por Blocos")

tk.Label(root, text="Mensagem:").grid(row=0, column=0)
entry_msg = tk.Entry(root, width=50)
entry_msg.grid(row=0, column=1)

tk.Label(root, text="Chave:").grid(row=1, column=0)
entry_chave = tk.Entry(root, width=50)
entry_chave.grid(row=1, column=1)

btn_enc = tk.Button(root, text="Criptografar", command=btn_criptografar)
btn_enc.grid(row=2, column=0)

btn_dec = tk.Button(root, text="Descriptografar", command=btn_descriptografar)
btn_dec.grid(row=2, column=1)

text_saida = tk.Text(root, height=5, width=50)
text_saida.grid(row=3, column=0, columnspan=2)

root.mainloop()