import pandas as pd 

df = pd.read_excel('semua.xlsx')
# print(df['Nama'].values)
kumpulan_nama = df['Nama'].values
print(kumpulan_nama)