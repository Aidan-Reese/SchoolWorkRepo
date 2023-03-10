#!/usr/bin/python3

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from builtins import input
import numpy as np
import os
import sys
import getopt
import math


# --------------------------------------
# Import other py files for this package
# --------------------------------------

from LAS_sD import *
from Q_sD import *
from plotter_sD import *

# ---------------------------
# Compute Dot Product:  v1*v2
# ---------------------------

def dot(v1,v2):
    d = 0.
    for i in range(0,2):
        d += v1[i]*v2[i]
    return d
    
# -----------------------
# Mat-Vec Product: Ax
# -----------------------

def matVec(A,x):
    mV = np.array( [ 0. , 0. ] )
    for i in range(0,2):
        for j in range(0,2):
            mV[i] += A[i][j]*x[j]
    return mV
    
# ------------------------
# Compute residual: b - Ax
# ------------------------

def residual(A,x,b):
    r = np.array( [0. , 0. ] )
    for i in range(0,2):
        r[i] = b[i] - matVec(A,x)[i]
    return r

# -----------------------
# Search along a Residual
# -----------------------

def searchAlongResidual(A,x,b,ax):

    # Find the residual

    r = residual(A,x,b)

    # Normalize it

    norm = math.sqrt(r[0]*r[0] + r[1]*r[1])
    r[0] /= norm
    r[1] /= norm

    # Take steps along the residual of size alpha

    alpha = -10.
    dAlpha = 0.001

    # Start the search by evaluating Q at the beginning of the line search
    
    Qval0 = Q(A, [ x[0] + alpha*r[0] , x[1] + alpha*r[1] ], b )

    # Evaluate again after taking one step along the residual
    
    alpha += dAlpha

    Qval1 = Q(A, [ x[0] + alpha*r[0] , x[1] + alpha*r[1] ], b )

    # Step along the normalize residual in dAlpha increments, re-evaluating Q each time,
    # and watching for a hilltop or valley floor.

    while ( alpha < 10. ):

        # Take the step and evaluate
        
        alpha += dAlpha
        
        Qval2 = Q(A, [ x[0] + alpha*r[0] , x[1] + alpha*r[1] ], b )

        # Look for the hilltop or valley floor.

        if (Qval1-Qval0)*(Qval1-Qval2) > 0.:
            alpha -= dAlpha/2.

            # Scale the residual so we can update the guess to the solution
    
            r *= alpha

            # Update the guess to the solution
    
            newGuess = x + r

            # Plot the distance we just moved, i.e., plot the alpha-scaled r.

            plotSearchResult(A,b,x,r,ax)

            return newGuess
        
        Qval0 = Qval1
        Qval1 = Qval2


    print("Search along residual never found an extremum.  Failing here.")
    val = input("Press <enter> to end.")
    
    exit(0)



# ==
# ||
# || Main Program
# ||
# ==

def steepestDescent(argv):

    # -------------------------------------------
    # Set up options for linear systems to study
    # -------------------------------------------

    # System 1:

    A1 = np.array( [
        [ 1. , 0. ],
        [ 0. , 1. ]
    ] )
    
    b1 = np.array( [ 0., 0.] )

    # System 2:

    A2 = np.array( [
        [ 10. , 3. ],
        [ 3. , 1. ]
    ] )
    
    b2 = np.array( [ 10., 0.] )

    # System 3:   

    A3 = np.array( [
        [ 10. , 3. ],
        [ 3. , 1. ]
    ] )
    
    b3 = np.array( [ 0., 0.] )

    # System 4:

#    A4 = np.array( [               #  <<<<<<  Students, establish a new case here
#        [   ,   ],
#        [   ,   ]
#    ] )
#    
#    b4 = np.array( [   ,  ] )

    # ----------------------------------------------------
    # Choose System and Adjust Q-Surface Evaluation Range
    # ----------------------------------------------------

    A = A3                         #  <<<<<<<<  Students, select the case here
    b = b3

    xRange =  [  -3.  ,   3. ]     #  <<<<<<<<  Students, you may need to adjust 
    yRange =  [  -3.  ,   3. ]     #            these for better plotting

    # ----------------------------
    # Set up data for plotting [1]
    # ----------------------------

    # 2D grid in the x-y plane

    xp,yp,xpp,ypp = setGrid(xRange,yRange,20)

    # The Q function to be minimized/maximized: Q = xb - (1/2) xAx

    zpp = np.array( Qs(A,b,xp,yp) )

    # --------------------------
    # Plot Setup [1]
    # --------------------------

    # Establish 3-D plot
    
    fig = plt.figure()
    
    ax = fig.gca(projection ='3d')
    fig.show()
    ax.set_title('xb -  (1/2) xAx')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    # --------------------------
    # Plot the Q surface
    # --------------------------
    
    ax.plot_surface(xpp, ypp, zpp, cmap ='viridis', edgecolor ='green',alpha=.4)
    fig.show()

    # ------------------------------------------------
    # Initial Guess for Ax = b solution (min/max of Q)
    # ------------------------------------------------

    solution = np.array ( [ 2., 2. ] )

    # --------------------------
    # Steepest Descent
    # --------------------------

    maxIter = 40
    for iter in range(0,maxIter):

        # -----------------------------
        # Convergence Check
        # -----------------------------
        
        r = residual(A,solution,b)

        if math.sqrt(r[0]*r[0] + r[1]*r[1]) < 0.01:
            print ("Steepest Descent Converged in " + str(iter) + " iteraations.  Solution is [x,y] = ",solution)
            val = input("Press <enter> to end.")
            return
    
        # ---------------------------------------
        # Not converged: Update solution and plot
        # ---------------------------------------

        solution = searchAlongResidual(A,solution,b,ax)
    
        fig.show()

    # --------------------------
    # Non-Convergence Outcome
    # --------------------------

    print ("Steepest Descent did not Converge.")
    val = input("Press <enter> to end.")

    return



if __name__ == "__main__":
    steepestDescent(sys.argv[1:])



    
# [1] https://www.geeksforgeeks.org/three-dimensional-plotting-in-python-using-matplotlib/
