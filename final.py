import pa6
from random import randint

def solve_QR(A, b):
    # create Q
    u = pa6.gram_schmidt(A)
    Q = pa6.Matrix(u)
    R_rowsp = []

    # Use col(A) and col(Q) to computer R where every elm is <aj, ui>
    # note both A and Q are the same size
    for i in range(len(Q.rowsp)):
        row = []
        for j in range(len(Q.colsp)):
            if i <= j:
                elm = Q.rowsp[i] * A.rowsp[i] 
            else:
                elm = 0
            row.append(elm)
            # add vector to R's rowspace
        row = pa6.Vec(row)
        R_rowsp.append(row)
    R = pa6.Matrix(R_rowsp) # nxn matrix

    # Transpose Q
    temp_qT_rowsp = [temp_qT_rowsp.append(row) for row in Q.rowsp]
    listQT = [temp_qT_rowsp] # temp list
    listQ = [Q.rowsp] 
    qT = []
    for i in range(len(Q.rowsp)):
        for j in range(len(Q.colsp)):
            listQT[j][i] = listQ[i][j]
        qT.append(pa6.Vec(listQT[i]))
    Q_transpose = pa6.Matrix(qT) # mxn matrix

    # Find inverse of  R

    # Find x
    x = R_inverse * Q_transpose * b # where b is in Rn
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
