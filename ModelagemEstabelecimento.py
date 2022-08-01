import pandas as pd
import glob


def limparcnpj(nome):
    nome = nome.replace('.', '').replace('/', '').replace('-', '').replace('.', '')
    return nome

folder_path = 'venv/download/'

file_list = glob.glob(folder_path + "*.csv")
main_dataframe = pd.DataFrame(pd.read_csv(file_list[0],sep = ';', encoding = 'utf-8',engine='c'))


for i in range(1,len(file_list)):
    data = pd.read_csv(file_list[i],sep = ';')
    df = pd.DataFrame(data)
    main_dataframe = pd.concat([main_dataframe,df])


main_dataframe_ajustado=main_dataframe
main_dataframe_ajustado['CNPJ da Revenda'] = main_dataframe['CNPJ da Revenda'].apply(limparcnpj)
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
df_ajustado=main_dataframe_ajustado.assign(cnpj_basico = cnpj_basico.str.slice(start=1, stop=9, step=1))
df_ordenado = df_ajustado[['cnpj_completo','cnpj_basico','revenda','regiao_sigla','estado_sigla','municipio','rua','numero','complemento','bairro','cep']]                                 
print(df_ordenado)
