import numpy as np
import matplotlib.pyplot as plt
def f(t):
    return np.exp(-t**2)
x = np.linspace(0,50,1000)
N = 100
a = np.zeros(1000)
b = x
h = (b-a)/N
k = int(N/2)
s = f(a) + f(b)
for i in range(1,k+1):
    s += 4*f(a + (2*i- 1)*h)
for i in range(1,k):
    s += 2*f(a + 2*i*h)
plt.plot(x,s*h/3)
plt.show()