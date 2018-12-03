import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from sklearn.cluster import KMeans

X=np.array([[1,2],[1.5,1.8],[5,8],[8,8],[1,0.6],[9,11]])
##plt.scatter(X[:,0], X[:,1], s=150) [:,0]means all the 0th elements in X
##plt.show()

clf= KMeans(n_clusters=2)
clf.fit(X)

centroids = clf.cluster_centers_
labels = clf.labels_ #labels=y for teh attrib X, essentially its 0,1 ie two clusters

colors=["r.","b."]

for i in range(len(X)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize=25)
    #labels[i] means that what label is that ith element and accordingly print its color
plt.scatter(centroids[:,0], centroids[:,1], marker= 'x', s=150, linewidths= 5)
plt.show()
