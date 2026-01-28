import tkinter as tk
from tkinter import messagebox, ttk

def calcular_preco_venda(custo, margem_percentual=40):
    margem_decimal = margem_percentual / 100
    return custo / (1 - margem_decimal)

def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

def calcular():
    print("Botão calcular pressionado")

def limpar():
    entry_custo.delete(0, tk.END)

janela = tk.Tk()
janela.title("Calculadora de Precificação - V2.0")
janela.geometry("600x650")
janela.configure(bg="#f5f7fa")

frame_header = tk.Frame(janela, bg="#2c3e50", height=120)
frame_header.pack(fill="x")
frame_header.pack_propagate(False)

tk.Label(frame_header, text="Calculadora de Precificação", 
        font=("Segoe UI", 22, "bold"), fg="#ffffff", bg="#2c3e50").pack(pady=(20, 5))
tk.Label(frame_header, text="Margem fixa de 40%",
        font=("Segoe UI", 11), fg="#bdc3c7", bg="#2c3e50").pack()

frame_conteudo = tk.Frame(janela, bg="#f5f7fa")
frame_conteudo.pack(pady=30, padx=30, fill="both", expand=True)

tk.Label(frame_conteudo, text="Custo do Produto (R$):",
        font=("Segoe UI", 12, "bold"), bg="#f5f7fa", fg="#2c3e50").pack(anchor="w")
entry_custo = tk.Entry(frame_conteudo, font=("Segoe UI", 16), relief="solid", borderwidth=1)
entry_custo.pack(fill="x", pady=5)

frame_botoes = tk.Frame(frame_conteudo, bg="#f5f7fa")
frame_botoes.pack(fill="x", pady=20)

btn_calcular = tk.Button(frame_botoes, text="CALCULAR", font=("Segoe UI", 12, "bold"),
        bg="#3498db", fg="white", command=calcular)
btn_calcular.pack(side="left", fill="x", expand=True, ipady=10, padx=(0, 5))

btn_limpar = tk.Button(frame_botoes, text="LIMPAR", font=("Segoe UI", 12, "bold"),
        bg="#95a5a6", fg="white", command=limpar)
btn_limpar.pack(side="left", fill="x", expand=True, ipady=10, padx=(5, 0))

frame_resultados = tk.Frame(frame_conteudo, bg="white", relief="groove", borderwidth=1)

if __name__ == "__main__":
    janela.mainloop()