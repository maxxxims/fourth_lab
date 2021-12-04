import sympy as sy

r, lmbd, u = sy.symbols('r, l, u')
A = sy.Matrix.zeros(9, 9)

A[0, 3] = -1 / r
A[1, 4] = -1 / r
A[2, 5] = -1 / r
A[3, 0] = -(lmbd + 2 * u)
A[6, 0] = -lmbd
A[8, 0] = -lmbd
A[4, 1] = -u
A[5, 2] = -u
A = sy.Matrix(A)

print(*A.eigenvals().items(), sep='\n')