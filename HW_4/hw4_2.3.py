import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BarycentricInterpolator

# Function to compute Chebyshev nodes
def chebyshev_nodes(n, a, b):
    return 0.5*(a + b) + 0.5*(b - a)*np.cos(np.pi*(2*np.arange(n) + 1)/(2*n))

# Compute Chebyshev nodes for the interval [0, pi/2] and n = 4
n = 4
a = 0
b = np.pi/2
nodes = chebyshev_nodes(n, a, b)

# Compute the values of sin at these nodes
values = np.sin(nodes)

# Construct the interpolating polynomial
polynomial = BarycentricInterpolator(nodes, values)

# Plot the polynomial and sin function on the interval [-2, 2]
x_values = np.linspace(-2, 2, 400)
plt.plot(x_values, polynomial(x_values), label='Chebyshev Interpolating Polynomial')
plt.plot(x_values, np.sin(x_values), label='sin(x)')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Chebyshev Interpolating Polynomial vs sin(x)')
plt.show()
