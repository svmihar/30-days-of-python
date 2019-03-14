from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import seaborn as sns
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

iris = load_iris()

# df = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
#                      columns= iris['feature_names'] + ['target'])
# print(df.head())
# df_cor = df.corr()
# sns.heatmap(df_cor, annot=True)
# plt.show()

from sklearn.datasets import make_moons

X, y = make_moons(n_samples=10000, noise=0.4, random_state=42)

plt.scatter(X[:,1],X[:,0])
plt.show()