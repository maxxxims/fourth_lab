import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from scipy.integrate import solve_ivp
from sympy import Function, dsolve, Eq, Derivative, symbols, lambdify



def func(x, y):
    return -2*y

############################################ SYMPY ############################################
x = symbols('x')
y = symbols('y', cls=Function)
s = dsolve(Eq(y(x).diff(x), - 2*y(x)), y(x), ics={y(0): np.sqrt(2)})
Y1 = lambdify(x, s.rhs, 'numpy')

print(str(s))

############################################ SCIPY ############################################
Y2 = solve_ivp(func, [0, 10], [sqrt(2)])


fig, (ax12, ax1, ax2) = plt.subplots(ncols=3)

ax12.plot(Y2.t, Y1(Y2.t) - Y2.y[0])
ax12.grid()
ax12.set_title('Sympy - Scipy')

x_span = np.linspace(0, 10, 1000)
ax1.plot(x_span, Y1(x_span), label=str(s.lhs) + ' = ' + str(s.rhs))
ax1.grid()
ax1.set_title('Sympy')

ax2.plot(Y2.t, Y2.y[0])
ax2.grid()
ax2.set_title('Scipy')

plt.savefig('result.png')
plt.show()

