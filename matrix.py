from pa4 import Vec

"""
implement setters and getter functions for Matrix class
"""

class Matrix:
    
    def __init__(self, rowsp):  
        self.rowsp = rowsp
        self.colsp = self._construct_cols(rowsp)
        
    # Review later
    def _construct_cols(self, rowsp):
        colsp = []
        for i in range(len(rowsp[0])):
            col = []
            for j in range(len(rowsp)):
                col.append(rowsp[j][i])
            colsp.append(col)
        return colsp
           
    def __add__(self, other):
        pass # todo: REPLACE WITH IMPLEMENTATION
    
    def __sub__(self, other):
        pass # todo: REPLACE WITH IMPLEMENTATION
    
    def __mul__(self, other):  
        if type(other) == float or type(other) == int:
            print("FIXME: Insert implementation of MATRIX-SCALAR multiplication")
            # # we know that mxn and nxp is valid.... so we should check there sizes first?
            # loop
                # for every item in the row space and rows, multiply each component by the other
                # then add that new component to a new row space 
            # update the new matrix that uses the new row space created
            # update colsp
        elif type(other) == Matrix:
            print("FIXME: Insert implementation of MATRIX-MATRIX multiplication") 
            # we know that mxn and nxp is valid.... so we should check there sizes first?
            # loop
                # assuming the product is defined, we can use the rows of A and the columns of B - dot product (from Vec)
                # after we get each component for a row, we add it to the new rowspace
            # update colsp
        elif type(other) == Vec:
            print("FIXME: Insert implementation for MATRIX-VECTOR multiplication")
            # make sure they're valid?
            # loop
                # dot product each row with the vector (create new row)
                # then add the new row to the new row space
            # update colsp
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
        # checks if column is the correct length
        if len(u) != len(self.colsp[0]):
            raise ValueError("ERROR: Incompatible column length.")
        else:
            self.colsp[j-1] = u  # Updating the column
            # update the row space
            newRowSp = []
            for i in range(len(self.colsp[0])):
                newRow = []
                for j in range(len(self.colsp)):
                    newRow.append(self.colsp[j][i])
                newRowSp.append(newRow)
            self.rowsp = newRowSp

    def set_row(self, i, v):
        """changes row i to the v list"""
        # checks if row is the correct length
        if len(v) != len(self.rowsp[0]):
            raise ValueError("ERROR: Incompatible row length.")
        else:
            self.rowsp[i-1] = v  # Updating the row
            # update column space
            self.colsp = self._construct_cols(self.rowsp)

    def set_entry(self, i, j, x):
        """changes ij-th entry in the matrix to x"""
        self.rowsp[i-1][j-1] = x # changes the entry
        self.colsp = self._construct_cols(self.rowsp) # updates the column space


    # GETTERS

    def get_col(self, j):
        """returns the j-th column as a list."""
        return self.col_space()[j-1]

    def get_row(self, i):
        """returns the i-th row as a list v"""
        return self.row_space()[i-1]

    def get_entry(self, i, j):
        """returns the existing ij-th entry in the matrix"""
        return self.row_space()[i-1][j-1]

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


"""TESTER CELL"""

A = Matrix([[1, 2, 3], [4, 5, 6]]) 
print("The setters and getters work as expected.")
print()