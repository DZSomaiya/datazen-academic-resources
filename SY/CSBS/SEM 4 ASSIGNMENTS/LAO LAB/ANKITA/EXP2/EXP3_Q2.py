#Q2) Verify whether 3 vectors in R^2 are linearly independent using rank.
#v1=(1,2)
#v2=(3,4)
#v3=(1,0)
import numpy as np
from numpy.linalg import matrix_rank
A = np.array([[1,2],[3,4],[1,0]])
print("Rank of matrix A is:",matrix_rank(A))
A1 = len(A)
A2 = matrix_rank(A)
if(A2 == A1):
    print("Since rank is equal to number of vectors\nThe matrix is Linearly Independent")
elif(A2 < A1):
    print("Since rank is less than number of vectors\nThe matrix is Linearly Dependent")
B = np.array([[1,2],[2,4],[3,6]])
print("Rank of matrix B is:",matrix_rank(B))
B1 = len(B)
B2 = matrix_rank(B)
if(B2 == B1):
    print("Since rank is equal to number of vectors\nThe matrix is Linearly Independent")
elif(B2 < B1):
    print("Since rank is less than number of vectors\nThe matrix is Linearly Dependent")