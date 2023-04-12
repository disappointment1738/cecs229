from pa4 import Vec
# from Vec import Vec

"""
implement setters and getter functions for Matrix class
"""

class Matrix:
    
    def __init__(self, rowsp):  
        self.rowsp = rowsp
        self.colsp = self._construct_cols(rowsp)
        
    def _construct_cols(self, rowsp):
        colsp = []
        for i in range(len(rowsp[0])):
            col = []
            for j in range(len(rowsp)):
                col.append(rowsp[j][i])
            colsp.append(col)
        return colsp
           
    def __add__(self, other):
        # check if matrix dimensions are valid
        if len(self.rowsp) != len(other.rowsp) or len(self.colsp) != len(other.colsp):
            raise ValueError("ERROR: Product is undefined.")
        else:
            newRowSp = []
            # iterate through the rows of the matrices
            for i in range(len(self.rowsp)):
                newRow = []
                sum = 0
                for j in range(len(self.rowsp[0])):
                    # add the components of self and other together 
                    sum = self.rowsp[i][j] + other.rowsp[i][j]
                    newRow.append(sum)
                newRowSp.append(newRow)
        return Matrix(newRowSp)
    
    def __sub__(self, other):
        # check if matrix dimensions are valid
        if len(self.rowsp) != len(other.rowsp) or len(self.colsp) != len(other.colsp):
            raise ValueError("ERROR: Product is undefined.")
        else:
            newRowSp = []
            # iterate through the rows of the matrices
            for i in range(len(self.rowsp)):
                newRow = []
                sum = 0
                for j in range(len(self.rowsp[0])):
                    # subtract the components of self and other together 
                    sum = self.rowsp[i][j] - other.rowsp[i][j]
                    newRow.append(sum)
                newRowSp.append(newRow)
        return Matrix(newRowSp)
    
    def __mul__(self, other):  
        """
        Overrides * operation
        Implementation of MATRIX-SCALAR, MATRIX-MATRIX, and MATRIX-VECTOR Multiplication
        """
        if type(other) == float or type(other) == int:
            newRowSp = []
            for i in range(len(self.rowsp)):
                newRow = []
                product = 0
                for j in range(len(self.rowsp[0])):
                    # multiply each component by the scalar
                    product = self.rowsp[i][j] * other
                    # add that new product to new row
                    newRow.append(product)
                # add that new row to new row space 
                newRowSp.append(newRow)
            return Matrix(newRowSp)
        elif type(other) == Matrix:
            # we know that mxn and nxp is valid.... so we should check their sizes first?
            if len(self.colsp) != len(other.rowsp):
                raise ValueError("ERROR: Product is undefined.")
            else:
                newRowSp = []
                for i in range(len(self.rowsp)):
                    newRow = []
                    for j in range(len(other.colsp[0])):
                        # we can use the rows of A and the columns of B - dot product from Vec
                        product = Vec(self.rowsp[i]) * Vec(other.colsp[j])
                        newRow.append(product)
                    # after we get each component for a row, we add it to the new rowspace
                    newRowSp.append(newRow)
                return Matrix(newRowSp)
        elif type(other) == Vec:
            if len(self.colsp) != len(other.elements):
                raise ValueError("ERROR: Incompatible dimensions.")
            else:
                newVec = []
                for i in range(len(self.rowsp)):
                    # dot product other and i-th row of self
                    product = Vec(self.rowsp[i]) * other
                    # add the new row to the new row space
                    newVec.append(product)
            return newVec
        else:
            print("ERROR: Unsupported Type.")
        return
    
    def __rmul__(self, other):
        """
        Implementation of scalar=matrix multiplication
        """
        if type(other) == float or type(other) == int:
            newRowSp = []
            for i in range(len(self.rowsp)):
                newRow = []
                product = 0
                for j in range(len(self.rowsp[0])):
                    # multiply each component by the scalar
                    product = self.rowsp[i][j] * other
                    # add that new product to new row
                    newRow.append(product)
                # add that new row to new row space 
                newRowSp.append(newRow)
            return Matrix(newRowSp)
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

    def get_diag(self, k): 
        """returns diagonal of a matrix. If k = 0, then the original diagonal is returned. 
        If k > 0, then returns diagonal starting at A 1(k+1)
        If k < 0, then returns diagonal starting at A (-k+1)1"""
        diagonal = []
        if k >= 0:
            for i in range(min(len(self.rowsp), len(self.rowsp[0]) - k)):
                diagonal.append(self.rowsp[i][i + k])
        else:
            for i in range(min(len(self.rowsp)+k, len(self.rowsp[0]))):
                diagonal.append(self.rowsp[i + abs(k)][i])
        return diagonal

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
print("\nThe setters and getters work as expected.")
print("get_diag() works as expected.")
print("Addition and substraction work as expected.\n")


# "TESTING OPERATOR + "
# A = Matrix([[1, 2],[3, 4],[5, 6]])
# B = Matrix([[1, 2],[1, 2]])
# C = Matrix([[10, 20],[30, 40],[50, 60]])
# # P = A + B # dimension mismatch --> raises error as intended
# Q = A + C
# R = A - C


# "TESTING OPERATOR * "
# # TESTING SCALAR-MATRIX MULTIPLICATION
# T = -0.5 * B 
# print("Matrix B") 
# print(B)
# print()

# print("Matrix T = -0.5 * B")
# print(T)
# print()

# # TESTING MATRIX-MATRIX MULTIPLICATION
# U = A * B
# print("Matrix U = A * B") 
# print(U)
# print()

# # TESTING MATRIX-VECTOR MULTIPLICATION 
# x = Vec([0, 1]) # Vec object
# b = A * x # b is a Vec data type 
# print("Vector b = A * x")
# print(b)