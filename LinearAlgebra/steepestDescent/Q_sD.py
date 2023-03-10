#!/usr/bin/python3

from LAS_sD import *
import numpy as np

# -----------------------
# Compute Q(x)
# -----------------------

def Q(A,x,b):

    # x dot b:

    x_dot_b = dot(x,b)

    # (1/2) x^T A x

    Ax = matVec(A,x)

    xAx = dot(x,Ax)

    # Q

    answer = x_dot_b - 0.5*xAx

    return answer


# --------------------------
# Compute Q at a point [x,y]
# --------------------------

def Qsurface(A,b,x,y):

    Qval = Q( A ,[ x,y ] , b )

    return Qval


# -------------------------------------
# Compute Q for an array of x,y values
# -------------------------------------

def Qs(A,b,x,y):

    surf = []

    for i in range(0,len(x)):
        row = []
        for j in range(0,len(y)):
            row.append( Q( A , [x[i],y[j]] , b ) )
        surf.append(row)

    return surf

