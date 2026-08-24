#importing libraries
import pandas as pd
import numpy as np

#importing dataset
data = pd.read_csv("breast-cancer_modified.csv")
data = data.select_dtypes(include=[np.number])

#X = all initial coulumns, y = last column (diagnosis)
X = data[data.columns[:-1]].values
y = data[data.columns[-1]].values
m, n = X.shape

#z = w^TX +b
z=np.dot(X,y)+b

#sigmoid function
def sigmoid(z):
    return 1/(1+np.exp(-z))

#cost function
def cost(y,y_pred):
    return

#gradient function
def gradient_descent(x,y,alpha,iteration):
   

    return w,b,cost_history


#newtons method
def newton_method(x,y,alpha,iterations):

    return w,cost_history

