import pa6
from random import randint

def solve_QR(A, b):
    # make A a set
    aSet = [pa6.Vec(row) for row in A.rowsp]
    # create Q
    u = pa6.gram_schmidt(aSet)
    Q = pa6.Matrix([ui.elements for ui in u])
    R_rowsp = []
    # Use col(A) and col(Q) to computer R where every elm is <aj, ui>
    # note both A and Q are the same size
    for i in range(len(Q.rowsp)):
        row = []
        for j in range(len(Q.colsp)):
            elm = 0
            if i <= j:
                elm = pa6.Vec(Q.rowsp[i]) * pa6.Vec(A.colsp[j])
            else:
                elm = 0
            row.append(elm)
            # add vector to R's rowspace
        row = pa6.Vec(row)
        R_rowsp.append(row)
    R = pa6.Matrix([row.elements for row in R_rowsp]) # nxn matrix

    # Transpose Q
    QTrowsp = []
    for i in range(len(Q.colsp)):
        row = []
        for j in range(len(Q.rowsp)):
            row.append(Q.rowsp[j][i])
        QTrowsp.append(row) 
    Q_transpose = ([row.elements for row in QTrowsp]) # mxn matrix

    # Use backwards substitution to solve R * x = Q_transpose * b
    n = R.rowsp # num of rows in R
    x = [0 for i in range(len(n))] # create "vector" of unknowns
    c = Q_transpose * b # product of matrix-vector mult.
    for i in range(n-1, -1, -1):
        s = 0 # temp variable, helps calculate num of remaining unknowns
        for j in range(i+1, n):
            s += R.rowsp[i][j] * x[j]
        x[i] = (c.elements[i]-s) / R.rowsp[i][i]
    x = pa6.Vec(x)
    return x






  
"""TESTER CELL"""
n = randint(3, 5)

rowsp = [[randint(-30, 30) for i in range(n)] for j in range(n)]
while not pa6.is_independent([pa6.Vec(row) for row in rowsp]):
    rowsp = [[randint(-30, 30) for i in range(n)] for j in range(n)]
    
A = pa6.Matrix(rowsp)
x_true = pa6.Vec([randint(-10, 10) for i in range(n)])
b = A * x_true
print("Expected:", x_true)

x = solve_QR(A, b)
print("Returned:", x)
