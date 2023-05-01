# problem 1, copy and paste Vec and Matrix classes, then add the needed methods.
"""Vector class"""
import numpy as np
import sys
class Vec:
    def __init__(self, contents = []):
        """
        Constructor defaults to empty vector
        INPUT: list of elements to initialize a vector object, defaults to empty list
        """
        self.elements = contents
        return
    
    def __abs__(self):
        """
        Overloads the built-in function abs(v)
        returns the Euclidean norm of vector v
        """
        sum = 0
        # iterate over the elements of contents
        for element in self.elements:
            sum += element ** 2
        sum = sum ** 0.5 # square root of sum
        return sum
        
    def __add__(self, other):
        """Overloads the + operator to support Vec + Vec
         raises ValueError if vectors are not same length
        """
        sum = []
        # check the precondition
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors are not same length")
        # add the elements of each vector
        for sNum, oNum in zip(self.elements, other.elements):
            sum.append(sNum + oNum)
        sum = Vec(sum) # convert array to Vec object?
        return sum
        
    def __sub__(self, other):
        """
        Overloads the - operator to support Vec - Vec
        Raises a ValueError if the lengths of both Vec objects are not the same
        """
        difference = []
        # check the precondition
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors are not same length")
        # subtract the elements of each vector
        for sNum, oNum in zip(self.elements, other.elements):
            difference.append(sNum - oNum)
        difference = Vec(difference) # convert array to Vec object?
        return difference
    
    def __mul__(self, other):
        """Overloads the * operator to support 
            - Vec * Vec (dot product) raises ValueError if vectors are not same length in the case of dot product
            - Vec * float (component-wise product)
            - Vec * int (component-wise product)
        """
        if type(other) == Vec: #define dot product
            # check the precondition
            if len(self.elements) != len(other.elements):
                raise ValueError("Vectors are not same length")
            dot = 0
            # iterate over both vectors
            for sNum, oNum in zip(self.elements, other.elements):
                new = sNum * oNum # mult. both
                dot += new # add them to the total
            return dot
        elif type(other) == float or type(other) == int: #scalar-vector multiplication
            product = []
            # mult. each component of vec by other (float or int)
            for element in self.elements:
                product.append(other * element) # mult. other and element, then add to list
            product = Vec(product) # convert array to Vec object?
            return product
    
    def __rmul__(self, other):
        """Overloads the * operation to support 
            - float * Vec
            - int * Vec
        """
        product = []
        # mult. each component of vec by other (float or int)
        for element in self.elements:
            product.append(other * element) # mult. other and element, then add to list
        product = Vec(product) # convert array to Vec object?
        return product
    
    # added methods go here
    def norm(self, p: int) -> float:
        """Finds the L-p norm of a vector"""
        # create temp/result variable 
        result = 0.0
        # add and apply p power to every component
        for elm in self.elements:
            num = abs(elm) ** p # apply the power of p to the (positive) component
            result += num # add to the result
        result = result ** (1/p) # apply 1/p power to the added components
        return result

    def __str__(self):
        """returns string representation of this Vec object"""
        return str(self.elements) # does NOT need further implementation

"""Matrix class"""
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
                    for j in range(len(other.colsp)):
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
            return Vec(newVec)
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

    # added methods go here
    def ref(self):
        """Applies Gaussian Elimination to a matrix. Returns matrix object"""
        a = self.row_space()
        a = a.list()
        n = len(a.col_space()[0]) # num of supposed unknown variables 
        # turn matrix into a upper triangular matrix
        for i in range(n):
            if a[i][i] == 0:
                raise ZeroDivisionError
            for j in range(i + 1, n):
                ratio = a[j][i] / a[i][i]
                for k in range(n + 1):
                    a[j][k] = a[j][k] - ratio * a[i][k]
        return Matrix(a)

    def rank(self):
        """returns the rank of A"""
        if type(self) != Matrix:
            raise ValueError
        matrix = self.ref()
        n = len(matrix.row_space())
        rank = 0
        for vec in matrix.row_space():
            if vec is all(0): # a zero vector
                pass
            else:
                rank += 1
        return rank

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

# problem 2
def gauss_solve(A, b):
    """
    Solves system Ax = b.
    If the system has a unique solution, it returns the solution as a Vec object.
    If the system has no solution, it returns None.
    If the system has infinitely many solutions, it returns the number of free variables (int) in the solution.
    """
    # make augmented matrix, Ab
    Ab = Matrix(np.concatenate(A, b.T, axis = '1'))
    # apply gaussian elimination (use ref())
    Ab.ref()
    # track positions of pivots (or keep track of them by using int) --> no of free is same as num of zero rows
    pivots = Ab.rank() 
    col = len(Ab.col_space())
    n = len(Ab.row_space())
    # if system has num of pivots = num of columns, then it is unique
    if pivots == col:
        for k in range(n - 2, -1, -1):
            pass
    # if system has num of pivots < num of columns, then it returns num of free variables (num of col - num of pivots)
    elif pivots < col:
        pass
    # if system is inconsistent, etc. returns None
    else:
        return None

# problem 3
def is_independent(S): 
    """Returns True if set S of V is linearly indep. Otherwise returns False"""
    # each vector in S is a column of the matrix
    # true if the solution is unique and not the zero vector
    # use gauss_solve()
    # if type is Vec and all elements are 0, return True
    # if type isn't a a Vec or has a nonzero element, return False
    pass

# problem 4
def gram_schmidt(S): 
    """
    Applies Gram-Schmidt process to create an orthogonal set of vectors. 
    Raise ValueError when set is not linearly indep.
    """
    # check precondition
    if not is_independent(S):
        raise ValueError("Invalid set of vectors.")
    # assigment variables
    uSet = set()
    wSet = set()
    w1 = S[0]
    u1 = w1 / w1.norm(2)
    uSet.add(u1)
    # compute the other vectors
    for i in range(1, len(S)):
        wS = Vec()
        # summation thingy
        for j in range(2, len(S)-1):
            wS = Vec()
        w = S[i-1] - wS
        wSet.add(w)
    # normalise all of the w vectors
    for i in range(len(wSet)):
        u = wSet[i] / wSet[i].norm(2)
        uSet.add(u)
    return uSet