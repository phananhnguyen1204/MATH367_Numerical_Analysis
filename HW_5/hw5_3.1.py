import numpy as np

# Data
years = np.array([1960, 1970, 1990, 2000])
populations = np.array([3039585530, 3707475887, 5281653820, 6079603571])

# Adjust years for the models (shifting the base year to 1960)
t = years - 1960

# Linear model
# y = a + b(t - 1960)
coeffs_linear = np.polyfit(t, populations, 1)
linear_model = np.polyval(coeffs_linear, t)
rmse_linear = np.sqrt(np.mean((populations - linear_model) ** 2))
pop_1980_linear = np.polyval(coeffs_linear, 1980 - 1960)

# Parabolic model
# y = a + b(t - 1960) + c(t - 1960)^2
coeffs_parabola = np.polyfit(t, populations, 2)
parabola_model = np.polyval(coeffs_parabola, t)
rmse_parabola = np.sqrt(np.mean((populations - parabola_model) ** 2))
pop_1980_parabola = np.polyval(coeffs_parabola, 1980 - 1960)

# Print results
print("Linear Model:")
print("Coefficients:", coeffs_linear)
print("RMSE:", rmse_linear)
print("Estimated population for 1980:", pop_1980_linear)
print("======================================================================================")

print("\nParabolic Model:")
print("Coefficients:", coeffs_parabola)
print("RMSE:", rmse_parabola)
print("Estimated population for 1980:", pop_1980_parabola)
print("======================================================================================")
print("\nThe parabolic model provides a better fit to the data based on the lower RMSE. ")
