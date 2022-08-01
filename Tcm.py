import requests
from bs4 import BeautifulSoup
import pandas as pd

target = "https://dados.gov.br/dataset/serie-historica-de-precos-de-combustiveis-por-revenda/"

headers ={
    'authority': 'app.mybodygallery.com',
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?1',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36'
}
response = requests.get(target,headers=headers)
content = response.content
site = BeautifulSoup(content, 'html.parser')

Lista_nome  = []

# Classes principais - Descrição e link do botão
resultados_classes = site.findAll('li', attrs={'class': 'resource-item'})

for resultado in resultados_classes:
  # Título
    descricao = resultado.find('a', attrs={'class': 'heading'})
    referencias = resultado.find('a', attrs={'class': 'resource-url-analytics'})
    Lista_nome.append([descricao.text.strip(), referencias['href']])

#Data Frame com resultado das classes        
resultados_dataframe = pd.DataFrame(Lista_nome, columns=['Descrição','Link'])
resultados_dataframe.reset_index()

#Definição dos critérios de filtro
criterio1 = resultados_dataframe[resultados_dataframe['Descrição'].str.contains('Etanol|\+ Gasolina Comum') & (resultados_dataframe['Descrição'].str.contains('2022'))]
criterio2 = resultados_dataframe[resultados_dataframe['Descrição'].str.contains('GLP|P13') & (resultados_dataframe['Descrição'].str.contains('2022'))]
criterio3 = resultados_dataframe[resultados_dataframe['Descrição'].str.contains('Diesel|S-500|\+Óleo') & (resultados_dataframe['Descrição'].str.contains('2022'))]

# identificação das colunas
criterio1.columns =['texto', 'link']
criterio2.columns =['texto', 'link']
criterio3.columns =['texto', 'link']

# Conversão para lista 
link1 = criterio1['link'].tolist()
link2 = criterio2['link'].tolist()
link3 = criterio3['link'].tolist()


for destino in link1:
  url = destino[56:]
  #Encontra o nome do arquivo para salvar
  if url.find('/'):
    arquivo = (url.rsplit('/', 1)[1])
  #Local de armazenamento  
  local_file = 'venv/download/'+arquivo
  data = requests.get(url,headers=headers)
  print(data)
  with open(local_file, 'wb')as file:
    file.write(data.content)

for destino in link2:
  url = destino[56:]
  #Encontra o nome do arquivo para salvar
  if url.find('/'):
    arquivo = (url.rsplit('/', 1)[1])
  #Local de armazenamento  
  local_file = 'venv/download/'+arquivo
  data = requests.get(url,headers=headers)
  print(data)
  with open(local_file, 'wb')as file:
    file.write(data.content)

for destino in link3:
  url = destino[56:]
  #Encontra o nome do arquivo para salvar
  if url.find('/'):
    arquivo = (url.rsplit('/', 1)[1])
  #Local de armazenamento  
  local_file = 'venv/download/'+arquivo
  data = requests.get(url,headers=headers)
  print(data)
  with open(local_file, 'wb')as file:
    file.write(data.content)