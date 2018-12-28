import pandas as pd 
import numpy as np 
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
dataset = pd.DataFrame([purchase_1,purchase_2,purchase_3], index=['Store 1','Store 2', 'Store 3']) 

dataset['Date'] = ['December 1', "December 2", "December 3" ]
dataset['Delivered'] = True
print(dataset.head())


""" Mergin dataframe with Set Theories """
staff_df = pd.DataFrame([
    {'Name': 'Kelly', 'Role': 'Director of HR'},
    {'Name': 'Sally', 'Role': 'Course Liason'},
    {'Name': 'James', 'Role': 'Grader'},
    ])
staff_df = staff_df.set_index('Name')
student_df = pd.DataFrame([
    {'Name': 'James', 'School': 'Business'},
    {'Name': 'Mike', 'School': 'Law'},
    {'Name': 'Sally', 'School': 'Engineering'}
])
student_df = student_df.set_index('Name')
print(staff_df)
print("\n", student_df)

""" Outer join """
print("\n Outer join \n", 
        pd.merge(staff_df,student_df,how="outer",left_index=True, right_index=True))

""" Inner join """
print("\n Inner join \n", 
        pd.merge(staff_df,student_df,how="inner",left_index=True, right_index=True))

""" Left join """
print("\n Left join \n", 
        pd.merge(staff_df,student_df,how="left",left_index=True, right_index=True))

dataset = pd.read_csv("suicide.csv")
print(dataset.head(5))
# dataset['sex'].replace('female', 1, inplace=True)
# dataset['sex'].replace('male', 0, inplace=True)
print(dataset['age'].unique())
print(dataset['country'].unique())
print(dataset.describe())
# for people in dataset['population'].unique():
#     avg = np.average(dataset.where())

""" pivot table of suicide dataset """
pivot_dataset = dataset.pivot_table(values='suicides_no', columns='sex', index="country", aggfunc=[np.mean, np.max, np.min], margins = True)
print(pivot_dataset)

