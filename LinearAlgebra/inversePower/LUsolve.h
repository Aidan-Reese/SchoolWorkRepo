
// ---------------------------------------------
// Solve (A - labmda I) xhat = x
// ---------------------------------------------

// A = LU, so solve the above system in a 2-step process

void LUsolve(double **L ,
	     double **U ,
	     double *Sol ,
	     double *RHS , int m , int n , double **A)
{
  double y   [n];

  // Solve L*y = x





  
  // Solve U*Sol = RHS



  

// Check solution LU * Sol = RHS, or Asave*Sol = RHS

  if ( n == m ) // Must be true for there to be a unique solution
    
    for ( int i = 0 ; i < m ; ++i )
      {
	double error = RHS[i];
	for ( int j = 0 ; j < n ; ++j )  error -= A[i][j]*Sol[j];

	if ( fabs(error) > 1.e-10 )
	  {
	    cout << "LU Solve failed\n";
	    exit(0);
	  }
      }
}

