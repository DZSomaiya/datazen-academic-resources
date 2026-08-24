import numpy as np
import pandas as pd
from numpy.linalg import matrix_norm

A = pd.read_csv("exp4.csv").values #import values of csv
m,n = A.shape #.shape function returns no. of rows and columns
print(m,n)
#OR
#m=A.shape[0] no. of rows
#n=A.shape[0] no. of columns

Q = np.zeros([m,n]) #initializing Q and R as zero matrices where Qm*n and Rn*n
R = np.zeros([n,n])
print(Q)
print(R)

for j in range(n):
    u = A[:j] #appending 2d array list; taking all first elements of the array

