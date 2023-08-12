import csv
import pandas as pd

# abrindo arquivo vazio CSV utilizando csv.reader(nome do arquivo)
with open('Personal Projects/LinkedIn/Relatório Automatizado/Vendas 1_2023.csv','r', encoding='utf-8') as arq:
    leitor = csv.reader(arq)
    
# abrindo arquivo para gravar conteúdo com csv.writer() e inserindo dados com csv.writerow()
with open('Personal Projects/LinkedIn/Relatório Automatizado/Vendas 1_2023.csv','a', encoding='utf-8') as arq:
    dados = csv.writer(arq)
    dados.writerow(('Produtos', 'Janeiro','Fevereiro', 'Março', 'Abril', 'Maio', 'Junho')) 
    dados.writerow(('Calça', 5, 7, 8, 9, 11, 15))
    dados.writerow(('Tênis', 3, 8, 10, 16, 7, 10))
    dados.writerow(('Bermuda', 5, 7, 8, 23, 6, 18))
    dados.writerow(('Boné', 14, 12, 8, 9, 20, 23))

# abrindo CSV com conteúdo gravado
with open('Personal Projects/LinkedIn/Relatório Automatizado/Vendas 1_2023.csv','r', encoding='utf-8') as arq:
    # lendo o CSV com função read_csv(nome do arquivo) do Pandas
    vendas = pd.read_csv(arq)

    # imprimindo o CSV lido em um DataFrame
    print(vendas)

    # exportando o DataFrame para o Excel com função to_excel(nome do arquivo) do Pandas
    vendas.to_excel('Personal Projects/LinkedIn/Relatório Automatizado/Vendas.xlsx', 
                sheet_name='1° semestre',
                index=False)
# sheet_name: para nomear planilha
# index = False -> para que os índices do DataFrame não sejam carregados para o Excel
