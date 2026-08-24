#Q3) Write a Python function to test linear independence of a given set of vectors. 
#v1=(1,0,0)
#v2=(0,1,0)
#v3=(0,0,1)
import numpy as np
from numpy.linalg import matrix_rank
A = np.array([[1,0,0],[0,1,0],[0,0,1]])
print("Rank of matrix B is:",matrix_rank(A))
A1 = len(A)
A2 = matrix_rank(A)
if(A2 == A1):
    print("Since rank is equal to number of vectors\nThe matrix is Linearly Independent")
elif(A2 < A1):
    print("Since rank is less than number of vectors\nThe matrix is Linearly Dependent")