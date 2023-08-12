import pandas as pd
from os import system

def clear():
    system('cls')

# Importando Excel com função read_excel(diretório) do Pandas
planilha = pd.read_excel('Personal Projects/LinkedIn/Relatório Automatizado/Vendas.xlsx')

# imprimindo planilha em um DataFrame para visualização
print(planilha, end='\n\n')

# Input para receber qual o mês 
mes = input('Qual mês deseja gerar relatório?\nInsira aqui: ')

# tratamento para Input
Mes = mes.capitalize()

clear()

# manipulação para trazer maior volume de vendas 
maior_venda = planilha.sort_values(by=f'{Mes}', ascending=False)
# ascending = False: por padrão, a ordenação é cresceste, mas com ascending = False 
# ordenamos de maneira decrescente

# localizando produto mais vendido pelo index com propriedade iloc[] do Pandas
# print(f'Maior venda ->', maior_venda.iloc[0,0].upper())
'''
iloc[0,0] para trazer o que está no index 0 tanto nas linhas, como nas colunas do dataframe
'''

# manipulação para trazer menor volume de vendas
menor_venda = planilha.sort_values(by=f'{Mes}')

# localizando produto menos vendido pelo index com propriedade iloc[] do Pandas
# print(f'Menor venda -> ', menor_venda.iloc[0,0].upper())

maior = maior_venda.iloc[0,0].upper()
menor = menor_venda.iloc[0,0].upper()

line = ('-'*20)

print(f'RELATÓRIO DE VENDAS\n{Mes.upper():>12}\n{line}\nMaior venda || {maior}\n{line}\nMenor venda || {menor}') 