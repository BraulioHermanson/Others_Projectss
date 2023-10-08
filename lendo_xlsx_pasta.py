import pandas as pd
import os
import getpass

# lendo arquivos .xlsx especificos de uma pasta
usuario = str(getpass.getuser())
path = r'C:/Users/'+ usuario +'/.../Pasta_Arquivo'
files = os.listdir(path)
files_origem = pd.DataFrame(files)

files_xlsx = [path + '\\' + f for f in files if f[-4:]=='xlsx']
df = []

for f in files_xlsx:
    df.append(pd.read_excel(f,header=0))

# dataframe gerado
df_principal = pd.concat(df,axis=0)

df_principal.head()

# gerando txt com os 5 ultimos arquivos adicionados na pasta
test_list = files_xlsx
delim = "\\"
res1, res2= [ele.split(delim)[0] for ele in test_list], [ele.split(delim)[1] for ele in test_list] 
with open('5_ultimos_desp_fora_P.txt', 'w', encoding='utf-8') as f:
    for line in res2[-5:]:
        f.write(line)
        f.write('\n')
