💼 Calculadora de Precificação

> Uma aplicação desktop robusta para cálculo de preço de venda baseada em margem de contribuição, desenvolvida com Python e Tkinter.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Tkinter](https://img.shields.io/badge/Interface-Tkinter-green)
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow)

## 📋 Sobre o Projeto

Este projeto visa auxiliar microempreendedores e autônomos na tarefa crítica de precificar produtos. Diferente de calculadoras comuns, este software utiliza o conceito de **Markup** para garantir que a margem de lucro seja real sobre o preço final de venda.

A versão atual conta com uma interface gráfica moderna, validação de dados e formatação automática para o padrão monetário brasileiro (BRL).

## ✨ Funcionalidades Atuais

-   🖥️ **Interface Gráfica (GUI):** Design limpo e intuitivo com *hover effects* e feedback visual.
-   🧮 **Cálculo Preciso:** Aplicação automática da fórmula de Markup (Custo / (1 - Margem)).
-   🛡️ **Tratamento de Erros:** Sistema robusto que previne falhas com inputs inválidos (ex: texto no lugar de números).
-   💲 **Formatação BRL:** Conversão automática de valores (ex: `1200.5` vira `R$ 1.200,50`).
-   ✨ **UX Refinada:** Navegação via teclado (Enter) e limpeza rápida de campos.

## 🚀 Como Executar

### Pré-requisitos
Certifique-se de ter o [Python](https://www.python.org/) instalado. O `tkinter` geralmente já vem incluído na instalação padrão do Python.

### Passo a Passo

1.  **Clone o repositório**
    ```bash
    git clone [https://github.com/seu-usuario/calculadora-precificacao-gui.git](https://github.com/seu-usuario/calculadora-precificacao-gui.git)
    ```
2.  **Entre na pasta**
    ```bash
    cd calculadora-precificacao-gui
    ```
3.  **Execute a aplicação**
    ```bash
    python main.py
    ```

## 🗺️ Roadmap (Próximas Atualizações)

O projeto está em evolução constante. Abaixo estão as funcionalidades planejadas para as próximas versões:

### v2.0 - Histórico e Sessão
- [ ] **Lista de Itens:** Adicionar uma tabela abaixo da calculadora que armazena cada cálculo feito na sessão atual.
- [ ] **Somatório Total:** Exibir o custo total e o lucro total projetado de todos os itens calculados na lista.

### v3.0 - Exportação de Dados
- [ ] **Gerar Relatório CSV:** Botão para exportar a lista de itens calculados para uma planilha Excel/CSV.
- [ ] **Orçamento em PDF:** Funcionalidade para gerar um arquivo `.pdf` pronto para impressão ou envio digital com a lista de preços.

## 🛠️ Tecnologias

* **Linguagem:** Python 3.12+
* **GUI:** Tkinter (Tcl/Tk)
* **Estilização:** Widgets nativos com customização de bordas e cores flat.

---
Desenvolvido por **Lavínia Morscheiter** 🚀
