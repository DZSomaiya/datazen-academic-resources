import numpy as np

#take user input for a matrix
n = int(input("Enter no. of rows for the matrix : "))
m = int(input("Enter no. of columns for the matrix : "))

A = []
i = 0
while i < n :
    v = []
    j = 0
    while j < m:
     v.append(int(input("Enter the element ")))
     j = j + 1
    A.append(v)
    i = i + 1

def SVD(A):
    #printing A
    print(A)
    #compute transpose of the matrix
    AT = np.transpose(A)
    print(AT)

    #AT*A
    X = AT@A
    print(X)

    #finding eigenvalue and eigenvector for X(AT*A)
    p,V = np.linalg.eig(X)
    print("Eigen values = ",p)
    print("Eigen vectors = ",V)

    #finding singular matrix
    singularmatrix = []
    for pi in p:
       si = np.sqrt(pi)
       singularmatrix.append(si)      
    print(singularmatrix)

    inv_singularmatrix = np.unique_inverse(singularmatrix)
    print(inv_singularmatrix)

    #finding U
    U = A @ V @ inv_singularmatrix
    print(U)  

SVD(A)









