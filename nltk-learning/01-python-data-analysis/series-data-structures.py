import pandas as pd 
animals = ["tiger", "bear", "moose"]
animals_series = pd.Series(animals)
print(animals_series) #dtype: object

numbers = [1,2,3,4]
numbers_series = pd.Series(numbers)
print(numbers_series) #dtype: int64

campur = [1,2,None]
campur_series = pd.Series(campur)
print(campur_series) #dtype: float64

import numpy as np 
np.nan == np.nan
np.isnan(np.nan)
 
class Person: 
    department = "school of information"

    def set_name(self, new_name):
        self.name = new_name
    def set_location(self, new_location):
        self.location = new_location

    my_function = lambda a,b,c : a+b
 


sports = {
        'Archery' : 'Bhutan',
        'Golf' : 'Scotland',     
        'Sumo' : 'Japan', 
        'Taekwondo': 'South Korea'
        }
s = pd.Series(sports)
print(s)

print(s.iloc[1])
print(s.loc['Golf'])
print(s[2])
print(s['Taekwondo'])

r = pd.Series([100.00,120.00,101.00,3.00])
print(r)
total = 0
for items in r:
    total += items
print(total)
#atau bisa pake sum di numpy
import numpy as np 
total = np.sum(r)
print(total)

#sum of random numbers in series
s = pd.Series(np.random.randint(0,1000,10000))
print(s.head())
print(len(s))
 # ingat kalau np.sum lebih cepet dari iterating total satu per satu 

