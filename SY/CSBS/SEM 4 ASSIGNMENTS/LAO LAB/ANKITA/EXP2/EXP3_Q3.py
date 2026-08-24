#Q3) Give an example of linearly dependent vectors and justify using rank.
#v1=(1,2,3)
#v2=(2,4,6)
#v3=(3,6,9)
import numpy as np
from numpy.linalg import matrix_rank
A = np.array([[1,2,3],[2,4,6],[3,6,9]])
print("Rank of matrix B is:",matrix_rank(A))
A1 = len(A)
A2 = matrix_rank(A)
if(A2 == A1):
    print("Since rank is equal to number of vectors\nThe matrix is Linearly Independent")
elif(A2 < A1):
    print("Since rank is less than number of vectors\nThe matrix is Linearly Dependent")
