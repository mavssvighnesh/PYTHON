import numpy as np 
import pandas as pd 

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

import  matplotlib.pyplot as plt
import seaborn as sns
iris_data=pd.read_csv('C:/Users/vighn/OneDrive/Documents/vv.csv')
iris_data
sns.countplot(iris_data['species'])
iris_data.plot(kind='scatter',x='sepal_length',y='sepal_width')
sns.set_style('whitegrid')
sns.FacetGrid(iris_data,hue ='species',size=6).map(plt.scatter,'sepal_length','sepal_width').add_legend()
sns.pairplot(iris_data,hue='species',size=2).add_legend()
for column in iris_data.columns:
    if iris_data[column].dtype==np.number:
        continue
iris_data[column]=LabelEncoder().fit_transform(iris_data[column])
iris_data.dtypes
iris_data.head()
x=iris_data.drop(['species'],axis=1)
y=iris_data['species']
x
y
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1)
k_range=list(range(1,12))
acc =[]
for i in k_range:
    knn=KNeighborsClassifier(n_neighbors=i).fit(x_train,y_train)
    y_pred=knn.predict(x_test)
    acc.append(metrics.accuracy_score(y_test,y_pred))
acc
knn=KNeighborsClassifier(n_neighbors=1).fit(x_train,y_train)
y_pred=knn.predict(x_test)
metrics.accuracy_score(y_test,y_pred)