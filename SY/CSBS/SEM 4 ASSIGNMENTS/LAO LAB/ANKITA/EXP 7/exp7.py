import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler

#take user input for a matrix
n = int(input("Enter no. of rows for the matrix : "))
m = int(input("Enter no. of columns for the matrix : "))

X = []
i = 0
while i < n :
    v = []
    j = 0
    while j < m:
     v.append(int(input("Enter the element ")))
     j = j + 1
    X.append(v)
    i = i + 1

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#user defined function
def my_pca(X,k):
   
   #calculating covariance matrix
   covmat = np.cov(X_scaled)
   print(covmat)
   
   #eigen decomposition of covariance matrix
   a,b = np.linalg.eig(covmat)
   eigenvalue = np.sort(a)
   
   #select top k eigen vectors
   eigenvector = b[:,:k]
   z = X_scaled@b
   
   return Z, eigenvalue
   my_pca(X,k)

z_custom, eigenvector =my_pca(X_scaled,k=2)
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
z_builtin = pca.fit_transform(X_scaled)
explained_varience = pca.explained_variance_ratio_

plt.scatter(z_custom[:,0], z_custom[:,1], label = "Custom PCA")
plt.title("PCA Project (User Defined)")
plt.xlable("PCA 1")
plt.ylable("PCA 2")
plt.legend()
plt.show()

plt.plot(explained_varience, marker = '0')
plt.title("Explained Varience Ratio")
plt.xlable("Principle Components")
plt.ylable("Varience")
plt.show()