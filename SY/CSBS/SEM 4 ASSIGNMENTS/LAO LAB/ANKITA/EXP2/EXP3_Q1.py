#Q1) Check linear independence of two vectors in R^2 using determinant
#v1=(1,2)
#v2=(3,4)
import numpy as np
from numpy.linalg import det
A1 = np.array([[1,2],[3,4]])
print("Determinanat of Matrix A is:",det(A1))
if det(A1) == 0:
    print("Since determinant is 0; the matrix is Linearly Dependent.")
else:
    print("Since determinant is not 0; the matrix is Linearly Independent.")
A2 = np.array([[10,4],[20,8]])
print("Determinanat of Matrix A is:",det(A2))
if det(A2) == 0:
    print("Since determinant is 0; the matrix is Linearly Dependent.")
else:
    print("Since determinant is not 0; the matrix is Linearly Independent.")
