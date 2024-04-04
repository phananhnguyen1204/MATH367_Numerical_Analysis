import numpy as np
from scipy.optimize import curve_fit

# Given data
months = np.arange(1, 13)
oil_used = np.array([6.224, 6.665, 6.241, 5.302, 5.073, 5.127, 4.994, 5.012, 5.108, 5.377, 5.510, 6.372])

# Normalize months to range [0, 1]
normalized_months = (months - 1) / 12

# Periodic model function
def periodic_model(t, c1, c2, c3, c4):
    return c1 + c2 * np.cos(2 * np.pi * t) + c3 * np.sin(2 * np.pi * t) + c4 * np.cos(4 * np.pi * t)

# Fit the model to the data
popt, _ = curve_fit(periodic_model, normalized_months, oil_used)

# Display the model
print(f"Function: y = {popt[0]:.4f} + {popt[1]:.4f} * cos(2*pi*t) + {popt[2]:.4f} * sin(2*pi*t) + {popt[3]:.4f} * cos(4*pi*t)")

# Calculate and display RMSE
predicted_values = periodic_model(normalized_months, *popt)
rmse = np.sqrt(np.mean((oil_used - predicted_values) ** 2))
print(f"RMSE: {rmse}")
