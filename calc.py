import tkinter as tk
from tkinter import messagebox

def calcular_preco_venda(custo, margem_percentual=40):
    margem_decimal = margem_percentual / 100
    return custo / (1 - margem_decimal)

def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

janela = tk.Tk()
janela.title("Calculadora de Precificação - V1.0")
janela.geometry("600x650")
janela.configure(bg="f5f7fa")

try:
    janela.iconbitmap("icon.ico")
except:
    pass

if __name__ == "__main__":
    janela.mainloop()