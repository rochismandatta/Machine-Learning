import numpy as np #numpy array is a list of lists or array of arrays
from sklearn import preprocessing, model_selection, neighbors, svm
import pandas as pd

df = pd.read_csv('breast-cancer-wisconsin.data.txt')#reading the data
df.replace('?', -99999, inplace=True)#replacing the missing values with outliers
df.drop(['id'],1, inplace=True)#dropping worthless attributes

X=np.array(df.drop(['class'],1)) #defining attributes 
y=np.array(df['class']) #defining labels or the thing we want to predict

#re-arranging the data using model selection
X_train, X_test, y_train, y_test =model_selection.train_test_split(X,y,test_size=0.2)

#Running the classifier algorithm
clf= svm.SVC()
#training the classifier
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy)


example_measures = np.array([4,2,1,1,1,2,3,2,1])
example_measures = example_measures.reshape(1,-1)
prediction = clf.predict(example_measures)
print(prediction)
