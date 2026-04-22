# To estimate the pi value
import numpy as np
r = l = 1
#points inside the square of length 1 
#to check if the point is inside the quartar circle
def pi_estimator(n):
    count = 0
    for i in range(n):
        x = np.random.rand()
        y = np.random.rand()
        if x**2 + y**2 <= 1:
            count += 1
    return 4*count/n
# area of quartar circle is 1/4 of pi for r = 1
#pi_estimate = area of square / area of quartar circle
n = 11111
pi_estimate = pi_estimator(n)
error = np.pi - pi_estimate
print(pi_estimate, error)