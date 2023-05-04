import pa6
from random import randint

def solve_QR(A, b):
    # todo
    pass
  
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
