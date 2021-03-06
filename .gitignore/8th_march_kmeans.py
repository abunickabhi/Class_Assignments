# -*- coding: utf-8 -*-
"""8th_March_kmeans.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1stRCn30WZLqGDZvYsgA6McNUTHzZYzPX
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

np.random.seed(5)
data = datasets.load_iris()
x = iris.data
y = iris.target
#print(iris)

def KMeans (k,data):
    centroids=random.sample(data,k)
    centroids=np.matrix(centroids)

    
distance_matrix = cdist(data,centroids,'euclidean')

data=list(datasets.data)

estimators = [('k_means_iris_8',KMeans(n_clusters=8)),('k_means_iris_3',KMeans(n_clusters=3)),('k_means_iris_3',KMeans(n_clusters=3))]
fign=1
for name,est in estimators:
    fig=plt.figure(fign,figsize=(4,3)) 
    ax = Axes3D(fig,rect=[0,0,0.95,1],elev=50,azim=130)
    est.fit(x)
    labels=est.labels_
    ax.scatter(x[:,3],x[:,0],x[:,2])
    ax.w_xaxis.set_ticklabels([])
    ax.w_yaxis.set_ticklabels([])
    ax.w_zaxis.set_ticklabels([])
    fign=fign+1
    
fig=plt.figure(fign,figsize=(4,3)) 
ax = Axes3D(fig,rect=[0,0,0.95,1],elev=50,azim=130)
for name , label in [('Sentosa',0),('Versicolor',1),('Se',0)]:
      ax.text3D(x[y==label,3].mean(),x[y==label,0].mean(),x[y==label,3].mean())
        
#fig.show()

