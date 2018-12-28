import pandas as pd 

purchase_1 = pd.Series({
    'Name': 'Sumihar',
    'Item Purchased' : 'Dog Food',
    'Cost': 22.5
    })
purchase_2 = pd.Series({
    'Name' : 'Christian',
    'Item Purchased' : 'Macbook Pro Retina 15 2015 CTO',
    'Cost' : 1500
    })
purchase_3 = pd.Series({
    'Name' : ' Natanael',
    'Item Purchased' : 'Apple 32\" Cinema Display',
    'Cost' : 200
    })
all = pd.DataFrame([purchase_1,purchase_2,purchase_3], index=['Store 1','Store 2', 'Store 3'])
# print(all)
# print(all.head())
# print(all.loc['Store 2'])
print("original")
print(all)

print("\ntransposed")
print(all.T)

print("\ntransposed only show cost row ")
print(all.T.loc['Cost'])


print("\n slicing dataframe, only shows name and cost value")
print(all.loc[:,["Name", "Cost"]]) # please dont do this. 

""" dropping columns """
copy_all = all.copy()
copy_all = copy_all.drop('Store 1')
print("\n dropping columns like it's hot")
print(copy_all)

""" #dropping columns pake inplace 
all.drop('Store 1', inplace = True)
print("\n dataframe all tapi di drop 1 dan inplace")
print(all)
 """

""" adding column """
print("\n add location in columns ")
all['Location'] = None
print(all)

""" 
DATA FRAME INDEXING, LOCATING
 """
cost = all['Cost']
print("\n only cost column")
print(cost)
data = pd.read_csv("suicide.csv", header=0)
data.reset_index()
# data.drop(0, inplace=True)
    # data.drop('1', inplace=True)
# print(data.iloc[0])

# """ Querying Dataframe """
# columns_to_keep = [
#     'No. Tilang', 
#     'Nama Terdakwa / Terpidana',
#     'Alamat Terdakwa / Terpidana', 
#     'Pasal Yang Dilanggar', 
#     'Barang bukti',
#     'No pol', 
#     'Denda (Rp)',
#     'Biaya Perkara (Rp)', 
#     'Jenis kendaraan', 
#     'Ket'
# ]
# data = data.columns[columns_to_keep]
# print("\n setelah dikurangi kolomnya ", data.head(5))
# print(data['age'])
# age = data['age']
# hitung = 0
# for i in age:
#     if(i == "5-15 years"):
#         print(i)
#         hitung+=1



data['sex'].replace('female', 1, inplace=True)
data['sex'].replace('male', 0, inplace=True)
print(data.head(5))
print(data.columns)
print(data.describe())
age = data.loc[:, 'age'].values
print(age)
from collections import Counter
print(Counter(age))
print(len(age))
# print(data.iloc[0:2])
# print(data.values)