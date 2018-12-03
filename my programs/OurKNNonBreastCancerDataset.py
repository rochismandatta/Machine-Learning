import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import warnings


def k_nearest_neighbors(data, predict, k=3): #k here is the number of keys of the dictionary, our dictionary has two keys of 3 points each in them
    if len(data)>=k:
        warnings.warn('K is set to a value less than total voting groups')
    distances=[]
    for group in data:
        # for group here we have k as a group type
        for features in data[group]:
            #traversing each coordinate inside a group eg: 'r'
            #euclidean_distance = np.sqrt(np.sum((np.array(featues)-np.array(predict))**2
            #however there is a better numpy code as compared to teh above code
            euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict)) 
            #the above line is just calculating distance entre each point in a group eg: 'r' to the entered set
            distances.append([euclidean_distance, group])
    votes= [i[1] for i in sorted(distances)[:k]]
    #print(Counter(votes).most_common(1))
    vote_result = Counter(votes).most_common(1)[0][0]
    return vote_result

df = pd.read_csv('breast-cancer-wisconsin.data.txt')
df.replace('?', -99999, inplace=True)
df.drop(['id'],1, inplace=True)
full_data = df.astype(float).values.tolist() #comverting the entire data to float type as well as to a list of lists

#print(full_data[:10])
random.shuffle(full_data) #C'est notre version de train_test and split

test_size=0.2
train_set = {2:[], 4:[]} #key is the label
test_set = {2:[], 4:[]}
train_data = full_data[:-int(test_size*len(full_data))] #everything upto the last 20% or 80%
test_data = full_data[-int(test_size*len(full_data)):]  # the last 20%

for i in train_data:
    train_set[i[-1].append(i[:-1])

''' # the 1st i[-1] the last column is the class column =2/4,
#appending the list to this list upto the last element(ie class) similar to df.drop['class']
'''
for i in test_data:
    test_set[i[-1].append(i[:-1])

correct=0

total=0

for group in test_set:
    for data in test_set[group]:
             vote= k_nearest_neighbors(train_set, data,k=5)
             if group==vote
             correct+=1
    total+=1
             
accuracy= correct/total
print(accuracy)
