
def get_desired_density(a, b, c, d, e, f):
    # Calculate the maximum number of grams of sugar that can be dissolved in water
    max_sugar = e * f // 100
    
    # Initialize the variables to track the best solution
    best_density = 0
    best_sugar = 0
    best_water = 0
    
    # Iterate over all possible combinations of sugar and water
    for sugar in range(c, d + 1):
        for water in range(a, b + 1):
            # Calculate the density of the current mixture
            density = (100 * sugar) / (water + sugar)
            
            # If the current mixture has a higher density than the best solution, update the best solution
            if density > best_density:
                best_density = density
                best_sugar = sugar
                best_water = water
    
    # Return the best solution
    return best_water, best_sugar

def main():
    # Read the input from stdin
    a, b, c, d, e, f = map(int, input().split())
    
    # Call the get_desired_density function and print the result
    water, sugar = get_desired_density(a, b, c, d, e, f)
    print(water, sugar)

if __name__ == '__main__':
    main()

