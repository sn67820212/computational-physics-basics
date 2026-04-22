# To find the value of integrand (np.sin(1/(x*(2-x))))**2dx over [0,2]
import numpy as np
def f(x):
    return (np.sin(1/(x*(2-x))))**2
N = 10000
count = 0
for i in range(N):
    x = 2*np.random.rand()
    y = np.random.rand()
    if y <= f(x):
        count += 1
I = 2*count/N
print("the value of integral is",I)
