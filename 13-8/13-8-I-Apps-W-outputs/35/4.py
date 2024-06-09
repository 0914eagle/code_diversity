
def check_package(n, a, b, c, d):
    # Check if a and b are valid
    if a - b < 0 or a + b > 1000:
        return "No"
    
    # Check if c and d are valid
    if c - d < 0 or c + d > 1000:
        return "No"
    
    # Calculate the sum of all possible weights
    sum_weights = (a + b) * n
    
    # Check if the sum of all possible weights is within the range of c and d
    if c - d <= sum_weights <= c + d:
        return "Yes"
    else:
        return "No"

