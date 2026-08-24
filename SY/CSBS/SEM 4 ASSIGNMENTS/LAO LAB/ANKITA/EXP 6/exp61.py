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
print(A)

#compute transpose of the matrix
AT = np.transpose(A)
print(AT)

#AT*A
X = AT@A
print(X)

#find eigenvalue and eigenvector for X(AT*A)
eigenval = np.linalg.eig(X)
print(eigenval)









