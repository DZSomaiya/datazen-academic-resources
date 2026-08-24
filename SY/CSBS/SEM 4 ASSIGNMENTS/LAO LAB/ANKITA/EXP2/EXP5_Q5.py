#Q5) Explain the relationship between rank and linear independence.
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
print("By *Rank Test* we can determine the Linear Dependence and Independence of vectors.\nWhen the rank is equal to no. of vectors we know all the vectors are linearly independent.\nThat is, their coefficients eg: k1x1+k2x2...+knxn=0 where k1=k2=...=kn=0.")