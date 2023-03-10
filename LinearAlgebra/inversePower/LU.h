

// --------------------------
// Forward Phase
// --------------------------



for ( int pivotRow = 0 ; pivotRow < m ; ++pivotRow ) 
  {
    pivotCol = findPivot(m,n, A, b, pivotRow,pivotRow);
    
    // Populate L during elimination
    //  .......
    
    
    // Now, eliminate
    
    for ( int elimRow = pivotRow + 1 ; elimRow < m ; ++ elimRow )
      {
      double fac = -A[elimRow][pivotCol]/A[pivotRow][pivotCol];

      L[pivotRow][pivotCol] = 1; //Populating LI with 1
      L[elimRow][pivotCol] = fac; //Populating the lower triangle with Fac

      for ( int col = pivotCol ; col < n ; ++col ) A[elimRow][col] += A[pivotRow][col] * fac;
      
      b[elimRow] += b[pivotRow] * fac;
      }
  }

// --------------------------
// Print Echelon Form
// --------------------------

printSystem("** Echelon Form **" , m , n , A  , b );
printSystem("** L **  "          , m , m , L  , b );

// --------------------------
// Check LU
// --------------------------

MatMat( L , m , A , n , m , LU );
printSystem("** LU Check **  "  , m , n , LU  , b );
