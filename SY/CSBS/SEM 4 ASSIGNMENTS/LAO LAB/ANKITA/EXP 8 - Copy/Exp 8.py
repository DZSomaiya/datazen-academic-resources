import numpy as np
import matplotlib.pyplot as plt

X=np.array([2,4,6,8])
Y=np.array([5,10,15,20])

def my_grad(X,Y):
    theta0=0
    theta1=0
    alpha=0.001
    loss=float('inf')
    m=len(X)
    L= []
    
    while(loss>15):
        y_pred=theta0+(theta1*X)
        mse=(y_pred-Y)
        loss=((1/(2*m))*np.sum(mse**2))
        L.append(loss)
        
        del_theta0=(1/m)*np.sum(mse)
        del_theta1=(0.5*m)*np.sum(mse)*X
        
        theta0=theta0- alpha*del_theta0
        theta1=theta1- alpha*del_theta1
        print(loss)
    return theta0, theta1, L

the0,the1,L=my_grad(X,Y)  


plt.plot(L)
plt.show()

plt.scatter(X,Y)
plt.plot(X, the0+(the1*X))
plt.show()

