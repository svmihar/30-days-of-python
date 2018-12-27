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
print("transposed")
print(all.T)
print("transposed ")
print(all.T.loc['Cost'])
