import numpy as np
import matplotlib.pyplot as plt

# Given data points
x_points = np.array([-1, 0, 3, 4, 5])
y_points = np.array([3, 5, 1, 1, 1])

# Number of splines
n = len(x_points) - 1

# System matrix and result vector
A = np.zeros((4*n, 4*n))
b = np.zeros(4*n)

# Building the system of equations
for i in range(n):
    # Spline equation at each x point
    xi = x_points[i]
    xi1 = x_points[i+1]
    
    A[2*i][4*i:4*i+4] = [xi**3, xi**2, xi, 1]
    A[2*i+1][4*i:4*i+4] = [xi1**3, xi1**2, xi1, 1]
    
    b[2*i:2*i+2] = [y_points[i], y_points[i+1]]

    if i < n - 1:
        # First derivative continuity
        A[2*n+i][4*i:4*i+4] = [3*xi1**2, 2*xi1, 1, 0]
        A[2*n+i][4*(i+1):4*(i+2)] = [-3*xi1**2, -2*xi1, -1, 0]

        # Second derivative continuity
        A[3*n+i-1][4*i:4*i+4] = [6*xi1, 2, 0, 0]
        A[3*n+i-1][4*(i+1):4*(i+2)] = [-6*xi1, -2, 0, 0]

# Natural spline condition: second derivative at end points is zero
A[-2][0:4] = [6*x_points[0], 2, 0, 0]
A[-1][-4:] = [6*x_points[-1], 2, 0, 0]

# Solve the system for coefficients
coefficients = np.linalg.solve(A, b)

# Function to evaluate the spline
def eval_spline(x, coefficients, x_points, n):
    for i in range(n):
        if x_points[i] <= x <= x_points[i+1]:
            a, b, c, d = coefficients[4*i:4*i+4]
            return a*x**3 + b*x**2 + c*x + d
    return None

# Plotting
x_range = np.linspace(np.min(x_points), np.max(x_points), 300)
y_range = [eval_spline(x, coefficients, x_points, n) for x in x_range]

plt.figure(figsize=(8, 6))
plt.plot(x_range, y_range, label='Natural Cubic Spline')
plt.scatter(x_points, y_points, color='red', label='Data Points')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Natural Cubic Spline Interpolation')
plt.legend()
plt.show()