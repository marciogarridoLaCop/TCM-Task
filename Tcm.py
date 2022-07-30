import requests
from bs4 import BeautifulSoup
import pandas as pd

target = "https://dados.gov.br/dataset/serie-historica-de-precos-de-combustiveis-por-revenda/"
response = requests.get(target)
content = response.content
site = BeautifulSoup(content, 'html.parser')

Lista_nome  = []
tipo01 = ["Etanol", "Gasolina","Comum"]
tipo02 = ["GLP P13"]
tipo03 = ["Óleo Diesel S-500","S-10","GNV"]
# Classes principais - Descrição e link do botão
resultados_classes = site.findAll('li', attrs={'class': 'resource-item'})

for resultado in resultados_classes:
  # Título
    descricao = resultado.find('a', attrs={'class': 'heading'})
    referencias = resultado.find('a', attrs={'class': 'resource-url-analytics'})
    Lista_nome.append([descricao.text.strip(), referencias['href']])

#Data Frame com resultado das classes        
resultados_dataframe = pd.DataFrame(Lista_nome, columns=['Descrição','Link'])

filtro01 = resultados_dataframe[resultados_dataframe.stack().str.contains('|'.join(tipo01)).any(level=0)]
filtro02 = resultados_dataframe[resultados_dataframe.stack().str.contains('|'.join(tipo02)).any(level=0)]
filtro03 = resultados_dataframe[resultados_dataframe.stack().str.contains('|'.join(tipo03)).any(level=0)]

print(filtro01)
print(filtro02)
print(filtro03)

#dados_filtrados.to_excel('TIPO1.xlsx', index=False)