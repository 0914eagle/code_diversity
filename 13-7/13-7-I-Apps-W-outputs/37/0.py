
def solve(n, k, a, b):
    # Calculate the total taste and total calories of the fruits
    total_taste = sum(a)
    total_calories = sum(b)
    
    # Check if it is possible to follow Inna's principle
    if total_taste % total_calories != 0:
        return -1
    
    # Calculate the maximum possible sum of the taste values of the chosen fruits
    max_taste = 0
    for i in range(n):
        max_taste += a[i] // b[i]
    
    # Check if the maximum possible sum of the taste values fulfills Inna's principle
    if max_taste * total_calories // total_taste == k:
        return max_taste
    else:
        return -1

