import requests
from bs4 import BeautifulSoup
import pandas as pd
import cfg as config

response = requests.get(config.target,headers=config.headers)
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
  local_file = config.folder_path+arquivo
  data = requests.get(url,headers=config.headers)
  print(data)
  with open(local_file, 'wb')as file:
    file.write(data.content)

for destino in link2:
  url = destino[56:]
  #Encontra o nome do arquivo para salvar
  if url.find('/'):
    arquivo = (url.rsplit('/', 1)[1])
  #Local de armazenamento  
  local_file = config.folder_path+arquivo
  data = requests.get(url,headers=config.headers)
  print(data)
  with open(local_file, 'wb')as file:
    file.write(data.content)

for destino in link3:
  url = destino[56:]
  #Encontra o nome do arquivo para salvar
  if url.find('/'):
    arquivo = (url.rsplit('/', 1)[1])
  #Local de armazenamento  
  local_file = config.folder_path+arquivo
  data = requests.get(url,headers=config.headers)
  print(data)
  with open(local_file, 'wb')as file:
    file.write(data.content)