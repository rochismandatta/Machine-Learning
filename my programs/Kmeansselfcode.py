import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np


X=np.array([[1,2],[1.5,1.8],[5,8],[8,8],[1,0.6],[9,11]])
##plt.scatter(X[:,0], X[:,1], s=150) [:,0]means all the 0th elements in X
##plt.show()

colors=["g","r","c","b","k"]

class K_Means:
    def __init__(self,k=2,tol=0.001,max_iter=300):
        self.k=k
        self.tol=tol
        self.max_iter= max_iter

    def fit(self,data):
        self.centroids ={}

        for i in range(self.k):
            self.centroids[i]=data[i]# setting the first 2 points as centroids

        for i in range(self.max_iter):
            self.classifications = {} #for this dictionary the keys is the centriods and the values are the feature sets

            for i in range(self.k):
                self.classifications[i]=[]

            for featureset in X:
                distances= [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
                #^creating a list of k=2 values where ist element and 2nd elements are the distances from datapoints to the centroids 0 and 1
                classification = distances.index(min(distances)) # index as in array index of the min value of distances
                self.classifications[classification].append(featureset)

            prev_centroids = dict(self.centroids)

            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification], axis=0)

                #^ the above code finds the mean of all the features and redefining the centroid
                
            optimized= True
            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]
                if np.sum((current_centroid-original_centroid)/original_centroid *100)>self.tol:
                    optimized= False
                if optimized:
                    break

                


                
    def predict(self,data):
        distances= [np.linalg.norm(data-self.centroid[centroid]) for centroid in self.centroids]
                
        classification = distances.index(min(distances))
        return classification

clf=K_Means()
clf.fit(X)

for centroid in clf.centroids:
    plt.scatter(clf.centroids[centroid][0],clf.centroids[centroid][1],
                marker="o", color ="k", s=150, linewidths =5)


for classification in clf.classifications:
    color=colors[classification]
    for featureset in clf.classifications[classification]:
        plt.scatter(featureset[0],featureset[1], marker ="x", color =color, s=150, linewidths=5)

plt.show()
        


        
                          
       
    
