import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

file_name = 'data.txt'
file = open(file_name, 'r')

i_ = 0
A = []
for line in file:
    if i_ == 0:
        n = int(line[:-1])
        i_+=1
    else:
        A.append(line.split(' '))


b = np.array(A[n])
A = np.array(A[:n], dtype=np.float64)
x = linalg.solve(A, b)

fig, ax = plt.subplots()
ax.bar(np.arange(1, n+1), x)
ax.grid(True)
plt.savefig('result.png')
plt.show()
