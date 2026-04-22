# h = (b-a)/n, k = [1,n]
# A_k = 1/2 * h * (f(a + (k-1) *h) + f(a + k*h))
# I = 1/2 * h sum((f(a + (k-1) *h) + f(a + k*h)))
# I= 1/2 * h * [f(a)+2f(a+h)+2f(a+2h)+...+2f(a+(n-1)h)+f(a+n*h)]
# I = h* [1/2f(a)+1/2f(b)+f(a+h)+f(a+2h)+...+f(a+(n-1)h)]
# Let us use the trapezoidal rule to calculate the integral of x 4 - 2x + 1 from x = 0 to x = 2.
def f(x):
    return x**4 - 2*x + 1

N = 1000
a = 0.0
b = 2.0
h = (b-a)/N
s = 0.5*f (a) + 0.5*f(b)
for k in range(1,N):
    s += f(a+k*h)
print(h*s)