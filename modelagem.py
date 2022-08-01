import pandas as pd
import glob
  
folder_path = 'venv/download/'

file_list = glob.glob(folder_path + "*.csv")
main_dataframe = pd.DataFrame(pd.read_csv(file_list[0],sep = ';', encoding = 'utf-8',engine='c'))


for i in range(1,len(file_list)):
    data = pd.read_csv(file_list[i],sep = ';')
    df = pd.DataFrame(data)
    main_dataframe = pd.concat([main_dataframe,df])


df_produtos = main_dataframe.iloc[:,10:11]
df_produtos.drop_duplicates(keep='first', inplace=True)
df_produtos.reset_index(drop=True, inplace=True)
print(df_produtos)
