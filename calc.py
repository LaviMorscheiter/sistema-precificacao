import tkinter as tk
from tkinter import messagebox, ttk

def calcular_preco_venda(custo, margem_percentual=40):
        margem_decimal = margem_percentual / 100
        return custo / (1 - margem_decimal)

def formatar_moeda(valor):
        return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

def animar_resultado():
        frame_resultados.configure(relief="solid", borderwidth=2)
        janela.after(100, lambda: frame_resultados.configure(relief="groove", borderwidth=1))

def calcular():
        try:
                entrada = entry_custo.get().replace(',', '.').replace('R$', '').strip()
                custo = float(entrada)
                if custo <= 0:
                        messagebox.showerror("Erro de Entrada", "Por favor, insira um valor de custo válido maior que zero.")
                        return
                preco_venda = calcular_preco_venda(custo)
                lucro = preco_venda - custo
                margem_percentual = (lucro / preco_venda) * 100
                label_custo_valor.config(text=formatar_moeda(custo))
                label_preco_valor.config(text=formatar_moeda(preco_venda))
                label_lucro_valor.config(text=formatar_moeda(lucro))
                label_margem_valor.config(text=f"{margem_percentual:.1f}%")
                frame_resultados.pack(fill="x", padx=30, pady=30)
                animar_resultado()
        except ValueError:
                messagebox.showerror("Erro", "Por favor, insira um número válido.\n\nExemplos: 100 ou 100,50")
                entry_custo.delete(0, tk.END)
                entry_custo.focus()

def limpar():
        entry_custo.delete(0, tk.END)
        label_custo_valor.config(text="R$ 0,00")
        label_preco_valor.config(text="R$ 0,00")
        label_lucro_valor.config(text="R$ 0,00")
        label_margem_valor.config(text="0%")
        frame_resultados.pack_forget()
        entry_custo.focus()

def ao_pressionar_enter(event):
        calcular()

def on_entry_focus_in(event):
        entry_custo.config(relief="solid", borderwidth=2)

def on_entry_focus_out(event):
        entry_custo.config(relief="solid", borderwidth=1)

def criar_hover_effect(widget, cor_normal, cor_hover):
        def on_enter(e):
                widget['background'] = cor_hover
        def on_leave(e):
                widget['background'] = cor_normal
                widget.bind("<Enter>", on_enter)
                widget.bind("<Leave>", on_leave)

janela = tk.Tk()
janela.title("💼 Calculadora de Precificação")
janela.geometry("800x850")
janela.minsize(800, 800)
janela.configure(bg="#f5f7fa")

frame_header = tk.Frame(janela, bg="#2c3e50", height=120)
frame_header.pack(fill="x")
frame_header.pack_propagate(False)

label_titulo = tk.Label(frame_header, text="Calculadora de Precificação", 
                font=("Segoe UI", 22, "bold"), fg="#ffffff", bg="#2c3e50")
label_titulo.pack(pady=(20, 5)) # titulo

label_subtitulo = tk.Label(frame_header, text="Margem de lucro de 40%",
                font=("Segoe UI", 11), fg="#bdc3c7", bg="#2c3e50")
label_subtitulo.pack() # subtitulo

linha = tk.Frame(frame_header, bg="#3498db", height=3)
linha.pack(fill="x", pady=(10, 0)) # linha decorativa

frame_conteudo = tk.Frame(janela, bg="#f5f7fa")
frame_conteudo.pack(pady=30, padx=30, fill="both", expand=True) # conteudo
frame_entrada = tk.Frame(frame_conteudo, bg="#f5f7fa")
frame_entrada.pack(fill="x", pady=(0,10)) # frame entrada
sombra_frame = tk.Frame(frame_conteudo, bg="#e0e0e0", height=2)
sombra_frame.place(in_=frame_entrada, rely=1.0, relwidth=1.0) # sombra
container_entrada = tk.Frame(frame_entrada, bg="#ffffff")
container_entrada.pack(fill="x", padx=25, pady=25) # container entrada

label_custo = tk.Label(container_entrada, text="💵 Custo do Produto:",
                font=("Segoe UI", 12, "bold"), bg="#ffffff", fg="#2c3e50")
label_custo.pack(anchor="w", pady=(0,8)) # label custo

frame_input = tk.Frame(container_entrada, bg="#ffffff")
frame_input.pack(fill="x") # frame input

entry_custo = tk.Entry(frame_input, font=("Segoe UI", 16), relief="solid", borderwidth=1, bg="#f8f9fa", fg="#2c3e50", insertbackground="#3498db")
entry_custo.pack(fill="x", pady=12)
entry_custo.focus()
entry_custo.bind("<Return>", ao_pressionar_enter)
entry_custo.bind("<FocusIn>", on_entry_focus_in) 
entry_custo.bind("<FocusOut>", on_entry_focus_out) # entrada custo

placeholder = "Ex:100,00"
label_placeholder = tk.Label(container_entrada, text=f"💡 {placeholder}", font=("Segoe UI", 9), bg="#ffffff", fg="#95a5a6")
label_placeholder.pack(anchor="w", pady=(5,0)) # placeholder

frame_botoes = tk.Frame(frame_conteudo, bg="#f5f7fa")
frame_botoes.pack(fill="x", pady=10)
btn_calcular = tk.Button(frame_botoes, text="📊 CALCULAR PREÇO", font=("Segoe UI", 12, "bold"), bg="#3498db", fg="white", activebackground="#2980b9", 
                        activeforeground="white", cursor="hand2", relief="flat",borderwidth=0, command=calcular)
btn_calcular.pack(side="left", fill="x", expand=True, ipady=15, padx=(0, 5))
criar_hover_effect(btn_calcular, "#3498db", "#2980b9") 

btn_limpar = tk.Button(frame_botoes, text="🗑️ LIMPAR", font=("Segoe UI", 12, "bold"), bg="#95a5a6", fg="white", activebackground="#7f8c8d",
                        activeforeground="white",cursor="hand2", relief="flat",borderwidth=0, command=limpar)
btn_limpar.pack(side="left", fill="x", expand=True, ipady=15, padx=(5, 0))
criar_hover_effect(btn_limpar, "#95a5a6", "#7f8c8d")

frame_resultados = tk.Frame(frame_conteudo, bg="#ffffff", relief="groove", borderwidth=1)
container_resultados = tk.Frame(frame_resultados, bg="#ffffff")
container_resultados.pack(fill="both", expand=True, pady=20, padx=25)

label_resultado_titulo = tk.Label(container_resultados, text="📈 ANÁLISE DE PRECIFICAÇÃO", font=("Segoe UI", 13, "bold"), bg="#ffffff", fg="#2c3e50")
label_resultado_titulo.pack(pady=(0, 15))

sep1 = ttk.Separator(container_resultados, orient='horizontal')
sep1.pack(fill='x', pady=(0, 15)) # separador

grid_resultados = tk.Frame(container_resultados, bg="#ffffff")
grid_resultados.pack(fill="x")

for i in range(4): # configurações de grid
        grid_resultados.grid_rowconfigure(i, weight=1)
        grid_resultados.grid_columnconfigure(0, weight=1)
        grid_resultados.grid_columnconfigure(1, weight=1)
        
tk.Label(grid_resultados, text="📦 Custo do Produto", font=("Segoe UI", 11), bg="#ffffff", fg="#555555", anchor="w").grid(row=0, column=0, sticky="w", pady=8)
label_custo_valor = tk.Label(grid_resultados, text="R$ 0,00", font=("Segoe UI", 11, "bold"), bg="#ffffff", fg="#e74c3c", anchor="e")
label_custo_valor.grid(row=0, column=1, sticky="e", pady=8) # custo valor

tk.Label(grid_resultados, text="🏷️ Preço de Venda", font=("Segoe UI", 11), bg="#ffffff", fg="#555555", anchor="w").grid(row=1, column=0, sticky="w", pady=8)

label_preco_valor = tk.Label(grid_resultados, text="R$ 0,00", font=("Segoe UI", 11, "bold"), bg="#ffffff", fg="#3498db", anchor="e")
label_preco_valor.grid(row=1, column=1, sticky="e", pady=8) # preço venda valor

sep2 = ttk.Separator(grid_resultados, orient='horizontal')
sep2.grid(row=2, column=0, columnspan=2, sticky="ew", pady=10) # separador

tk.Label(grid_resultados, text="💰 Lucro Bruto", font=("Segoe UI", 12, "bold"), bg="#ffffff", fg="#555555", anchor="w").grid(row=3, column=0, sticky="w", pady=8)
label_lucro_valor = tk.Label(grid_resultados, text="R$ 0,00", font=("Segoe UI", 12, "bold"), bg="#ffffff", fg="#27ae60", anchor="e")
label_lucro_valor.grid(row=3, column=1, sticky="e", pady=8) # lucro valor

tk.Label(grid_resultados, text="📊 Margem de Lucro", font=("Segoe UI", 11), bg="#ffffff", fg="#555555", anchor="w").grid(row=4, column=0, sticky="w", pady=8)
label_margem_valor = tk.Label(grid_resultados, text="0%", font=("Segoe UI", 11, "bold"), bg="#ffffff", fg="#f39c12", anchor="e")
label_margem_valor.grid(row=4, column=1, sticky="e", pady=8) # margem valor

frame_footer = tk.Frame(janela, bg="#ecf0f1", height=50)
frame_footer.pack(fill="x", side="bottom")
frame_footer.pack_propagate(False)
label_rodape = tk.Label(frame_footer, text="💡 Dica: Use vírgula ou ponto para decimais • Pressione ENTER para calcular", font=("Segoe UI", 9), bg="#ecf0f1", fg="#7f8c8d")
label_rodape.pack(expand=True) # rodapé

janela.update_idletasks()
largura = janela.winfo_width()
altura = janela.winfo_height()
x = (janela.winfo_screenwidth() // 2) - (largura // 2)
y = (janela.winfo_screenheight() // 2) - (altura // 2)
janela.geometry(f'{largura}x{altura}+{x}+{y}')
janela.mainloop() # executar aplicação