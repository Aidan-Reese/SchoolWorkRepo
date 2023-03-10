#!/usr/bin/python3
import numpy as np
from Q_sD import *


def vectorPlotQ(x0,x1,y0,y1,A,b):
    
    x = np.array( [x0, x1] )
    y = np.array( [y0, y1] )

    Q0 = Q(A, [x0 ,y0 ]  , b )
    Q1 = Q(A, [x1 ,y1 ]  , b )
    z = np.array( [Q0,Q1] )

    return x,y,z

def vectorPlot(x0,x1,y0,y1,z0,z1):
    
    x = np.array( [x0, x1] )
    y = np.array( [y0, y1] )

    z = np.array( [-.1,-.1] )

    return x,y,z

def plotSearchResult(A,b,x,r,ax):

    xp1,yp1,zp1 = vectorPlotQ(x[0]        ,  x[0]         ,  x[1]         ,  x[1]         ,  A    ,  b )
    xp2,yp2,zp2 = vectorPlotQ(x[0] + r[0] ,  x[0] + r[0]  ,  x[1] + r[1]  ,  x[1] + r[1]  ,  A    ,  b )

    xFinal = np.concatenate((xp1,xp2),axis=0)
    yFinal = np.concatenate((yp1,yp2),axis=0)
    zFinal = np.concatenate((zp1,zp2),axis=0)

    ax.plot3D(xFinal, yFinal, zFinal,linewidth = 3)


    
# ----------------------
# Set up Grid
# ----------------------

def setGrid(xRange,yRange,n):

    x0 = xRange[0]
    x1 = xRange[1]
    
    y0 = yRange[0]
    y1 = yRange[1]

    x = []
    y = []
    dx = (x1-x0)/(n-1)
    dy = (y1-y0)/(n-1)

    for i in range(0,n):
        x.append(x0+i*dx)
        y.append(y0+i*dy)

    # 1-D arrays that store the x-y locations for the grid
    
    xp = np.array( x )
    yp = np.array( y )

    # 2-D arrays that store each grid point

    xpp = []
    ypp = []
    for i in range(0,n):
        row = []
        col = []
        for j in range(0,n):
            row.append( xp[i] )
            col.append( yp[j] )
        xpp.append(row)
        ypp.append(col)

    return xp,yp,xpp,ypp

