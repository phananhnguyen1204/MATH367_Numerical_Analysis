import numpy as np

# Given data
years = np.array([1960, 1970, 1990, 2000])
populations = np.array([3039585530, 3707475887, 5281653820, 6079603571])

print("P(t) = P0 * e^(kt)")
print("Where P(t) is the population at year t, P0 is the initial population (at t=0), and k is the growth rate.")


# Linearization: Apply natural logarithm to the population
log_populations = np.log(populations)

# Perform linear regression to find the best fit line
slope, intercept = np.polyfit(years, log_populations, 1)

# Estimate the population for 1980 using the exponential model
predicted_population_1980 = np.exp(intercept + slope * 1980)

# Given actual population in 1980
actual_population_1980 = 4452584592

# Calculate estimation error
estimation_error = actual_population_1980 - predicted_population_1980

# Print out the calculated parameters and results
print(f"Slope (k): {slope}")
print(f"Intercept (ln(P0)): {intercept}")
print(f"Predicted Population in 1980: {predicted_population_1980}")
print(f"Estimation Error: {estimation_error}")