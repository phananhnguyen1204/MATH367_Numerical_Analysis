def newtdd(list_x, list_y, x,n):
    # Create 2D array of size n*n
    triangle = [[0 for x in range(n)] for y in range(n)]
    
    # Fill in y column of Newton triangle
    for r in range(0,n):
        triangle[r][0] = list_y[r]

    # Newtn Divided Difference   
    for j in range(1,n):
        # Fill in column from top to bottom
        for i in range(n-j):
            triangle[i][j] = (triangle[i+1][j-1] - triangle[i][j-1]) /(list_x[i+j] - list_x[i])
            

    n = len(list_x) - 1
    p = triangle[0][n]
    # Create polynomial 
    for k in range(1,n+1):
        p = triangle[0][n-k] + (x - list_x[n-k])*p
    return p

# Given data points
years = [1960, 1970, 1990, 2000]
population = [3039585530, 3707475887, 5281653820, 6079603571]
# Estimate the 1980 population
predict_result = newtdd(years, population,1980,len(population))
print("Prediction Result: " + str(predict_result))
# Population need to be an integer, round down the prediction result
estimated_1980_population = round(predict_result)
print("Estimated 1980 population using Newton Divided Differences Method: " + str(estimated_1980_population))
print("1980 population: ", 4452584592)
print("Difference : " + str(abs(estimated_1980_population - 4452584592)))