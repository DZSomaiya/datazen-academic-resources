#import libraries
import numpy as np
import pandas as pd

#read csv
data = [pd.read_csv("exp_8_dataset.csv").values]
print(data)

#user defined function for gradient descent
def my_grad(x,y):
    #initialize theta_0, theta_1
    theta_0 = 0
    theta_1 = 0
    while(J_theta < 1*10**-6):
        y_pred = theta_0 + theta_1*x
        for()
        