import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

class Support_Vector_Machine: #the innit method is the only method that runs default without calling in a class
    def __init__(self, visualization=True):
        self.visualization= visualization
        self.colors= {1:'r',-1:'b'}
        if self.visualization:
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(1,1,1)
            
#fit is essentially training and finding w and b through optimisation
    def fit(self,data):
        self.data = data
        # { ||w||: [w,b]}---> magnitude of w is the key and the values is w and b
        opt_dict = {}
        transforms = [[1,1],
                      [1,-1],
                      [-1,1],
                      [-1,-1]]

        all_data = []
        for yi in self.data:
            for featurset in self.data[yi]:
                for feature in featureset:
                    all_data.append(features)

        self.max_features_value = max(all_data)
        self.min_features_value = min(all_data)
        all_data=None


        step_sizes = [self.max_featues_value*0.1,
                      self.max_featues_value*0.01,
                      self.max_featues_value*0.001,]

        b_range_multiple = 5


        b_multiple = 5

        latest_optimum = self.max_feature_value*10

        for step in step_sizes:
             w = np.array([latest_optimum,latest_optimum])
             optimized=False

             while not optimized:
                 for b in np.arange(-1*(self.max_feature_value*b_range_multiple),
                                    self.max_feature_value*b_range_multiple,
                                    step*b_multiple):
                     for tranformations in transforms:
                         w_t = w*transformations
                         found_option = True
                         for i in self.data:
                             for xi in self.data[i]:
                                 yi=i
                                 if not yi*(np.dot(w_t,xi)+b) >=1
                                 found_option = False
                        
                        if found_option:
                            opt_dict[np.linalg.norm(w_t)] = [w_t,b]

                    if w[0] < 0:
                        optimized = True
                        print('Optimised a step')
                    else:
                        w=w-step
                norms=sorted([n for n in opt_dict])

                opt_choice = opt_dict[norms[0]]
                self.w= opt_choicep[0]
                self.b= opt_choice[1]
                latest_optimum = opt_choice[0][0]+ step*2
                     
                    

                 
             


        







        

    def predict(self,features):
#classification is essentially sign of (x.w+b)
        classification = np.sign(np.dot(np.array(features),self.w)+self.b)
        if classification !=0 and self.visualization:
            self.ax.scatter(features[0], features[1], s=200, marker =*, c=self.colors[classification])
        return classification

    def visualize(self):
        [[self.ax.scatter(x[0],x[1],s=100, color=self.colors[i]) for x in data_dict[i]]]


        def hyperplane(x,w,b,v):
            return (-w[0]*x-b+v) / w[1]


    datarange = self.min_feature_value*0.9, self
    


data_dict = {-1:np.array([[1,7],
                           [2,8],
                           [3,8],]),
             1:np.array([[5,1],
                         [6,-1],
                         [7,3],])}
