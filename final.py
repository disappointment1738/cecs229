import pa6
from random import randint

def solve_QR(A, b):
    aSet = set(pa6.Vec(row) for row in A.row_space())
    # create Q
    u = pa6.gram_schmidt(aSet) # throws error for A (type matrix has no len), but throws error when I try to use aSet (in construct cols???)
    Q = pa6.Matrix(u)
    R_rowsp = []

    # Use col(A) and col(Q) to computer R where every elm is <aj, ui>
    # note both A and Q are the same size
    for i in range(len(Q.rowsp)):
        row = []
        for j in range(len(Q.colsp)):
            if i <= j:
                elm = Q.rowsp[i] * A.rowsp[j] 
            else:
                elm = 0
            row.append(elm)
            # add vector to R's rowspace
        row = pa6.Vec(row)
        R_rowsp.append(row)
    R = pa6.Matrix(R_rowsp) # nxn matrix

    # Transpose Q
    temp_qT_rowsp = Q.rowsp.copy()
    listQT = [temp_qT_rowsp] # temp list
    listQ = [Q.rowsp] 
    qT = []
    for i in range(len(Q.rowsp)):
        for j in range(len(Q.colsp)):
            listQT[j][i] = listQ[i][j]
        qT.append(pa6.Vec(listQT[i]))
    Q_transpose = pa6.Matrix(qT) # mxn matrix

    # Use backwards substitution to solve R * x = Q_transpose * b
    n = R.rowsp # num of rows in R
    x = [0 for i in range(len(n))] # create "vector" of unknowns
    c = Q_transpose * b # product of matrix-vector mult.
    cList = [c] 
    rList = [R.rowsp]
    for i in range(n-1, -1, -1):
        s = 0 # temp variable, helps calculate num of remaining unknowns
        for j in range(i+1, n):
            s += rList[i][j] * x[j]
        x[i] = (cList[i]-s) / rList[i][i]
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
