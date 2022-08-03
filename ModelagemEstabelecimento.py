import pandas as pd
import glob
import cfg as config

file_list = glob.glob(config.folder_path + "*.csv")
main_dataframe = pd.DataFrame(pd.read_csv(file_list[0],sep = ';', encoding = 'utf-8',engine='c'))

for i in range(1,len(file_list)):
    data = pd.read_csv(file_list[i],sep = ';')
    df = pd.DataFrame(data)
    main_dataframe = pd.concat([main_dataframe,df])

main_dataframe_ajustado=main_dataframe
main_dataframe_ajustado['CNPJ da Revenda'] = main_dataframe['CNPJ da Revenda'].apply(config.limparcnpj)
df_precos = main_dataframe_ajustado.copy(deep=True)

main_dataframe_ajustado.rename(columns={'cnpj_basico':'cnpj_basico',
                                'CNPJ da Revenda': 'cnpj_completo',
                                'Revenda': 'revenda',
                                'Regiao - Sigla': 'regiao_sigla',
                                'Estado - Sigla': 'estado_sigla',
                                'Municipio': 'municipio',
                                'Nome da Rua': 'rua',
                                'Numero Rua': 'numero',
                                'Complemento': 'complemento',
                                'Bairro': 'bairro',
                                'Cep': 'cep'},                                  
                                inplace = True)
cnpj_basico=main_dataframe_ajustado['cnpj_completo']
main_dataframe_ajustado.assign(cnpj_basico = cnpj_basico)
main_dataframe_ajustado.to_csv('tmp/estabelecimentos.csv', sep = ';', index = True )

## Criação da tabela precos
df_produto= pd.read_csv('tmp/produto.csv',sep = ';')
df_produto.rename( columns={'Unnamed: 0':'id_produto'}, inplace=True )

def id(row):
    index = df_produto.index
    condition = df_produto["Produto"] == row['Produto']
    indice = index[condition].tolist()
    return indice.pop()

df_precos['id_produto'] = df_precos.apply(lambda row: id(row), axis=1)
df_precos.drop(columns=['Revenda','Produto','Regiao - Sigla','Estado - Sigla','Municipio','Nome da Rua','Numero Rua','Complemento','Bairro','Cep'], inplace = True)
df_precos.to_csv('tmp/precos.csv', sep = ';', index = True )
