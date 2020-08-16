import math
from math import comb #CALCULATOR CAN'T IMPORT COMB

print("Calculating coefficients of sequence in the form (A + Bx)^n")
A = int(input("A = "))
B = int(input("B = "))
n = int(input("n = "))

for r in range(n+1):
    
    C = comb(n, r) * (A**(n-r)) * (B**r)
    print("Coefficient of x to the power of " + str(r))
    print(C)
