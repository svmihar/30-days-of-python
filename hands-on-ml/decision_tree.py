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

from sklearn.model_selection import train_test_split, GridSearchCV
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2)
params = {'max_leaf_nodes': list(range(2, 100)), 'min_samples_split': [2, 3, 4]}

from sklearn.tree import DecisionTreeClassifier
grid_search_cv = GridSearchCV(DecisionTreeClassifier(random_state=42), params, n_jobs=-1, verbose=1, cv=3, scoring='neg_mean_squared_error')
grid_search_cv.fit(X_train, y_train)
print(grid_search_cv.best_params_)
cv_results = grid_search_cv.cv_results_

for mean_score, params in zip(cv_results['mean_test_score'], cv_results['params']): 
    print(np.sqrt(-mean_score), params)

from sklearn.metrics import accuracy_score

y_pred = grid_search_cv.predict(X_test)
score = accuracy_score(y_test, y_pred)
print(score)