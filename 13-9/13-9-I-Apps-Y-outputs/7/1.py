
def get_density(a, b, c, d, e):
    # Calculate the density of the sugar water
    density = (100 * b) / (a + b)
    
    # Calculate the amount of sugar dissolved in the water
    sugar_dissolved = density * e / 100
    
    return density, sugar_dissolved

def get_max_density(a, b, c, d, e, f):
    # Initialize the maximum density and the corresponding amount of sugar dissolved
    max_density = 0
    sugar_dissolved = 0
    
    # Iterate over the possible combinations of operations
    for i in range(101):
        for j in range(101):
            for k in range(101):
                for l in range(101):
                    # Calculate the density and the amount of sugar dissolved for the current combination of operations
                    density, sugar_dissolved = get_density(a, b, c, d, e)
                    
                    # Check if the current combination of operations achieves the maximum density and the amount of sugar dissolved is within the limit
                    if density > max_density and sugar_dissolved <= f:
                        max_density = density
                        sugar_dissolved = sugar_dissolved
    
    return max_density, sugar_dissolved

if __name__ == '__main__':
    # Read the input from stdin
    a, b, c, d, e, f = map(int, input().split())
    
    # Call the function to get the maximum density and the amount of sugar dissolved
    max_density, sugar_dissolved = get_max_density(a, b, c, d, e, f)
    
    # Print the output
    print(max_density, sugar_dissolved)

