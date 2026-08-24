import numpy as np
from numpy.linalg import norm 

def dotproduct():
    v1 = np.array([4,6,2])
    v2 = np.array([7,3,2])
    v3 = np.array([5,4,8])
    u1=v1 
    u2=v2-((v2.dot(u1))/(u1.dot(u1))*u1) #2
    print(u2)
    u3=v3-((v3.dot(u1))/(u1.dot(u1))*u1)-((v3.dot(u2))/(u2.dot(u2))*u2) #3
    print(u3)
    #u1,u2,u3 are orthogonal
    normu1 = norm(u1)
    normu2 = norm(u2)
    normu3 = norm(u3)
    q1=u1/normu1
    q2=u2/normu2
    q3=u3/normu3
    def print():
        q1,q2,q3
        print()
    dotproduct()