from pa4 import Vec # exclude in the notebook

"""
implement setters and getter functions for Matrix class
"""

class Matrix:
    
    def __init__(self, rowsp):  
        self.rowsp = rowsp
        self.colsp = self._construct_cols(rowsp)
        
    # FIX THIS
    def _construct_cols(self, rowsp):
        colsp = []
        col = []
        for row in rowsp:
            for i in range(2):
                for j in range(2):
                    col.append(rowsp[i][j])
            colsp.append(col)
        return colsp
           
    def __add__(self, other):
        pass # todo: REPLACE WITH IMPLEMENTATION
    
    def __sub__(self, other):
        pass # todo: REPLACE WITH IMPLEMENTATION
    
    def __mul__(self, other):  
        if type(other) == float or type(other) == int:
            print("FIXME: Insert implementation of MATRIX-SCALAR multiplication")  # todo
        elif type(other) == Matrix:
            print("FIXME: Insert implementation of MATRIX-MATRIX multiplication") # todo
        elif type(other) == Vec:
            print("FIXME: Insert implementation for MATRIX-VECTOR multiplication")  # todo
        else:
            print("ERROR: Unsupported Type.")
        return
    
    def __rmul__(self, other):  
        if type(other) == float or type(other) == int:
            print("FIXME: Insert implementation of SCALAR-MATRIX multiplication")  # todo
        else:
            print("ERROR: Unsupported Type.")
        return
    

    # SETTERS

    def set_col(self, j, u):
        """changes column j to the u list"""
        pass

    def set_row(self, i, v):
        """changes row i to the v list"""
        pass

    def set_entry(self, i, j, x):
        """changes ij-th entry in the matrix to x"""
        pass


    # GETTERS

    def get_col(self, j):
        """returns the j-th column as a list."""
        return self.col_space()[j]

    def get_row(self, i):
        """returns the i-th row as a list v"""
        return self.row_space()[i]

    def get_entry(self, i, j):
        """returns the existing ij-th entry in the matrix"""
        return self.row_space()[i][j]

    def col_space(self):
        """returns the list of vectors that make up the column space of the matrix object"""
        return self.colsp

    def row_space(self):
        """returns the list of vectors that make up the row space of the matrix object"""
        return self.rowsp

    def get_diag(self, k): # this one is yikes
        """returns diagonal of a matrix. If k = 0, then the original diagonal is returned. 
        If k > 0, then returns diagonal starting at A 1(k+1)
        If k < 0, then returns diagonal starting at A (-k+1)1"""
        pass

    def __str__(self):
        """prints the rows and columns in matrix form """
        mat_str = ""
        for row in self.rowsp:
            mat_str += str(row) + "\n"
        return mat_str
                
    def __eq__(self, other):
        """overloads the == operator to return True if 
        two Matrix objects have the same row space and column space"""
        return self.row_space() == other.row_space() and self.col_space() == other.col_space()

    def __req__(self, other):
        """overloads the == operator to return True if 
        two Matrix objects have the same row space and column space"""
        return self.row_space() == other.row_space() and self.col_space() == other.col_space()


A = Matrix([[1, 2, 3], [4, 5, 6]]) 
print("Original Matrix:")
print(A)
print()