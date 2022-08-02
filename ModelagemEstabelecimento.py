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

df_produto= pd.read_csv('tmp/produto.csv',sep = ';')
df_produto.columns.name = 'id'

print(df_produto)

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
cnpj_basico=main_dataframe_ajustado['cnpj_completo'].copy()
main_dataframe_ajustado.assign(cnpj_basico = cnpj_basico)
print(main_dataframe_ajustado)

#df_produtos = main_dataframe.iloc[:,10:11]
#df_estabelecimento=main_dataframe
#df_estabelecimento.drop_duplicates(keep='first', inplace=True)
#df_estabelecimento.reset_index(drop=True, inplace=True)
#print(df_estabelecimento)
