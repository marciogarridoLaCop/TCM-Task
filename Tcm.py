import requests
from bs4 import BeautifulSoup
import pandas as pd

target = "https://dados.gov.br/dataset/serie-historica-de-precos-de-combustiveis-por-revenda/"
response = requests.get(target)
content = response.content
site = BeautifulSoup(content, 'html.parser')

lista_nome  = []
listal_link = []
# Classes principais - 
resultados = site.findAll('li', attrs={'class': 'resource-item'})
links =site.findAll('div', attrs={'class': 'dropdown btn-group'})


for resultado in resultados:
  # Título
    descricao = resultado.find('a', attrs={'class': 'heading'})
    referencias = resultado.find('a', attrs={'class': 'resource-url-analytics'})
    lista_nome.append([descricao.text, referencias['href']])
    
resultados = pd.DataFrame(lista_nome, columns=['Descrição','Link'])
print(resultados)
