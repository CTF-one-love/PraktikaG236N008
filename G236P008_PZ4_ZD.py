#Решение симплексным методом задачи линейного программирования на языке Python
import numpy as np
import scipy as sp

c = [-1, -2, -1, 1, -6]
A = [[-1, 5, 1, 1, 1], [2, -1, 1, 3, 0], [0, 10, 1, 2, 3]]
b = [10,6,25]

x1 = (0, None)
x2 = (0, None)
x3 = (0, None)
x4 = (0, None)
x5 = (0, None)
from scipy.optimize import linprog
res = linprog(c, A_ub=A,b_ub=b, bounds=(x1,x2,x3,x4,x5),method='simplex', options={"disp": True})
print(res)
