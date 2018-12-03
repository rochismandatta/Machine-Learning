import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')

dataset = {'k':[[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]]}
new_features= [5,7]


'''for i in dataset:
    for ii in dataset[i]:
        plt.scatter(ii[0],ii[1], s=100, color=i)'''


#writing the above for loop in one line
'''
[[plt.scatter(ii[0],ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset]
plt.scatter(new_features[0], new_features[1])
plt.show()
'''

def k_nearest_neighbors(data, predict, k=3): #k here is the number of keys of the dictionary, our dictionary has two keys of 3 points each in them
    if len(data) >=k:
        warnings.warn('K is set to a value less than total voting groups')
    distances=[]
    for group in data:# for group here we have k as a group type
        for features in data[group]: #traversing each coordinate inside a group eg: 'r'
            #euclidean_distance = np.sqrt(np.sum((np.array(featues)-np.array(predict))**2
            #however there is a better numpy code as compared to teh above code
            euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict)) 
#the above line is just calculating distance entre each point in a group eg: 'r' to the entered set
            distances.append([euclidean_distance, group])
    votes= [i[1] for i in sorted(distances)[:k]]
    print(Counter(votes).most_common(1))
    vote_result = Counter(votes).most_common(1)[0][0]

    return vote_result

result = k_nearest_neighbors(dataset, new_features, k=3)
print(result)
