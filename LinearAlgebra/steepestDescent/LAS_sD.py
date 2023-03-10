#!/usr/bin/python3
import numpy as np

# -----------------------
# Compute Dot Product
# -----------------------

def dot(v1,v2):
    d = 0.
    for i in range(0,2):
        d += v1[i]*v2[i]
    return d
    
# -----------------------
# Mat-Vec Product
# -----------------------

def matVec(A,x):
    mV = np.array( [ 0. , 0. ] )
    for i in range(0,2):
        for j in range(0,2):
            mV[i] += A[i][j]*x[j]
    return mV
    
