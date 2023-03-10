#include "iPow.h"
#include "LUsolve.h"




// =========================================================================
// M A I N   P R O G R A M
// =========================================================================

int main(int argc, char *argv[])
{
  int m; // number of rows
  int n; // number of columns

  #include "setCase.h"

  // ---------------------------------------------
  // Set up Inverse Power Method
  // ---------------------------------------------

  int    iter      = //how many iterations
  int    maxIter   =  //max integer number
  int    converged = //flag on if youre converging on eigen val
  double tol       =  //10^-5 tolerance
  double mu;  
  double mu_old    = 
  double lambda; //goal

  double x[n];     // Used during Inverse Power Method Iteration, see class notes
  double xhat[n];  //   "   "       "       "      "      "        "    "     "

  // Compute initial guess at x
  
    for (int i = 0; i < n;i++) x[i] = 1/1+i; //giving x values of 1,1/2,1/3,1/4

  // Compute (A - alpha*I) and store in A.

    for (int k = 0; k <= n; k++) A[k][k] -= alpha;  //A[i][i] follows the diagnal

  // Save new A = (A - alpha*I) in Asave:

  Asave = A; //saving to Asave

  // Print (A - alpha*I)
  
  printSystem("(A-alphaI)",m,n,A,b);
  
  // ---------------------------------------------
  // Perform LU factorization of new A
  // ---------------------------------------------
  


  #include "LU.h"

  // A now stores what.?  Point to the upper triangular A with  U:

    double **U = A; //After calculating L A is now the upper triangle

  // ---------------------------------------------
  // Inverse Power Method Iterations
  // ---------------------------------------------

  while (  converged != 1 )
    {
      // Max iteration check
      
      if (iter>maxIter)    {exit(0)} //Too many itterations and youll exit
      iter++;
      // Step 2a: Compute xhat (Solve  (A - alpha I) * xhat = x)
      A = MatMat(L,n,U,n,n,A)
      xhat[iter] = xhat[iter-1]/A

      LUsolve(L , U , xhat , x , m , n , Asave );   // Asave is passed to check solution
      
      // Step 2b: Scale xhat so that the largest value = 1
      for(int l = 0; l < xhat.size(); l++){
        if(xhat[l]>muold){
          muold = xhat[l];
        }
      }
      mu=muold;
      for(int l1 = 0; l1 < xhat.size(); l1++){
        xhat[l1] = xhat[l1]/mu;
      }


      

      // Step 2c: Check for convergence
      

      cout << "iter = " << iter << " mu = " << mu << endl;
      
    }

  // Compute final estimate for eigenvalue of original A, Aoriginal:

    lambda = alpha + 1/mu;
  
    cout << caseName << ": Inverse Power Method Converged in " << iter << " iterations." << endl;
    cout << caseName << ": =========================== Results " << endl;
    cout << caseName << ": mu = " << mu << endl;
    cout << caseName << ": lambda = " << lambda << endl;
    cout << caseName << ": ===========================         " << endl;
  
  
  // ---------------------------------------------
  // Test Eigenvalue/Eigenvector
  // ---------------------------------------------

    // Print eigenvector and Aoriginal * eigenvector, computing the ratio
    // to see how consistent that ratio is.


    
    iLOOP printf("%s: E-vector Check:     x[%d] = %5.2f     Ax[%d] = %5.2f     ratio = %s\n",
		 caseName.c_str(), .....   );

    
    
  
}

