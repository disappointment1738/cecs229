import Vec from pa4

"""
implement setters and getter functions for Matrix class
"""

class Matrix:
    
    def __init__(self, rowsp):  
        self.rowsp = rowsp
        self.colsp = self._construct_cols(rowsp)
        
    def _construct_cols(self, rowsp):
        colsp = []
        # todo: INSERT YOUR IMPLEMENTATION HERE
        return colsp
           
    def __add__(self, other):
        pass # todo: REPLACE WITH IMPLEMENTATION
    
    def __sub__(self, other):
        pass # todo: REPLACE WITH IMPLEMENTATION
    
    # FUNCTIONS THAT DONT NEED EDITING
    
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
