import os
import time

def limpar_tela():
    """Função para limpar a tela em Windows, Mac ou Linux."""
    sistema = os.name
    if sistema == 'nt': # Windows
        os.system('cls')
    else: # Linux ou Mac
        os.system('clear')

def calcular_preco_venda(custo, margem_percentual=40):
    margem_decimal = margem_percentual / 100
    # Fórmula de margem bruta: Custo / (1 - Margem)
    return custo / (1 - margem_decimal)

# Limpa a tela antes de começar
limpar_tela()

while True:
    print("--- 🏢 CALCULADORA DE PRECIFICAÇÃO (Margem 40%) ---")
    print("Digite 'sair' para encerrar o programa.\n")
    
    entrada = input(">> Digite o custo do produto (R$): ")
    
    if entrada.lower() in ['sair', 'fim', 'exit']:
        print("\nEncerrando calculadora...")
        time.sleep(1)
        break
    
    try:
        # Substitui vírgula por ponto para aceitar input brasileiro (ex: 10,50)
        custo = float(entrada.replace(',', '.'))
        
        preco_venda = calcular_preco_venda(custo)
        lucro = preco_venda - custo

        print("\n" + "="*35)
        print(f"📦 Custo do Produto:  R$ {custo:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
        print(f"🏷️  Preço de Venda:    R$ {preco_venda:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
        print(f"💰 Lucro (40%):       R$ {lucro:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
        print("="*35 + "\n")

        # Pausa para leitura
        input("Pressione ENTER para calcular o próximo...")
        limpar_tela()
        
    except ValueError:
        print("\n❌ Erro: Digite apenas números válidos!")
        time.sleep(2)
        limpar_tela()