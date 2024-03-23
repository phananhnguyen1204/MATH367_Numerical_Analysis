import numpy as np
import matplotlib.pyplot as plt
import scipy.misc

# Data points
x_data = np.array([0.6, 0.7, 0.8, 0.9, 1.0])
y_data = np.array([1.433329, 1.632316, 1.896481, 2.247908, 2.718282])

# Function for divided differences
def divided_differences(x, y):
    n = len(y)
    f = np.zeros([n, n])
    f[:,0] = y
    for j in range(1, n):
        for i in range(n - j):
            f[i][j] = (f[i + 1][j - 1] - f[i][j - 1]) / (x[i + j] - x[i])
    return f

# Calculating divided differences
F = divided_differences(x_data, y_data)

# Function to construct the interpolation polynomial
def construct_polynomial(x, F):
    def polynomial(X):
        n = len(F)
        P = np.zeros_like(X)
        for i in range(n):
            term = F[0, i]
            for j in range(i):
                term *= (X - x[j])
            P += term
        return P
    return polynomial

# Constructing the polynomial P4(x)
P4 = construct_polynomial(x_data, F)

# Function to print actual value, error, and error bound
def print_error_info(x_val):
    actual_value = f(x_val)
    interpolated_value = P4(x_val)
    actual_error = actual_value - interpolated_value
    error_bound = max_fifth_derivative / np.math.factorial(5) * np.prod([x_val - xi for xi in x_data])

    print(f"x = {x_val}:")
    print(f"  Actual value of f({x_val}): {actual_value}")
    print(f"  Interpolated value P4({x_val}): {interpolated_value}")
    print(f"  Actual Error at {x_val}: {actual_error}")
    print(f"  Error Bound at {x_val}: {error_bound}\n")

# Actual function
def f(x):
    return np.exp(x**2)

# Fifth derivative for error bound
def fifth_derivative(x):
    return scipy.misc.derivative(f, x, n=5, order=7)

# Error bound estimation
x_range = np.linspace(0.5, 1, 1000)
max_fifth_derivative = max([fifth_derivative(x) for x in x_range])

# Calculating and printing the actual values, errors, and error bounds for each x in x_data
for x_val in x_data:
    print_error_info(x_val)

# Additional values to calculate and print
additional_x_values = [0.82, 0.98]
for x_val in additional_x_values:
    print_error_info(x_val)

# Function to calculate error for plotting
def interpolation_error(x):
    return f(x) - P4(x)

# Generating points for the plot
x_range_1 = np.linspace(0.5, 1, 500)
x_range_2 = np.linspace(0, 2, 500)
errors_1 = [interpolation_error(x) for x in x_range_1]
errors_2 = [interpolation_error(x) for x in x_range_2]

# Plotting errors
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(x_range_1, errors_1, label='Error on [0.5, 1]')
plt.title('Interpolation Error on [0.5, 1]')
plt.xlabel('x')
plt.ylabel('Error')
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x_range_2, errors_2, label='Error on [0, 2]')
plt.title('Interpolation Error on [0, 2]')
plt.xlabel('x')
plt.ylabel('Error')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
