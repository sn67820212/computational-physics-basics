# Reference:  Mark Neumann sec 5.1.2
# I(a,b) = 1/3 [f(a) + f(b) + 4 f((a+(2k-1)h + 2 f(a+2kh)]
def f(x):
    return x**4 - 2*x + 1

N = 100
a = 0.0
b = 2.0
h = (b-a)/N
k = int(N/2)
s = f(a) + f(b)
for i in range(1,k+1):
    s += 4*f(a + (2*i- 1)*h)
for i in range(1,k):
    s += 2*f(a + 2*i*h)
print(h*s/3)