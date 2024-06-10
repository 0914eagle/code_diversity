
def get_optimal_sugar_water(a, b, c, d, e, f):
    # Initialize the optimal solution
    optimal_solution = [0, 0]
    
    # Iterate over all possible combinations of operations
    for operation_1 in range(a + 1):
        for operation_2 in range(b + 1):
            for operation_3 in range(c + 1):
                for operation_4 in range(d + 1):
                    # Calculate the total mass of sugar and water in the beaker
                    total_sugar = operation_1 * 100 + operation_3 * c + operation_4 * d
                    total_water = operation_1 * 100 + operation_2 * 100
                    
                    # Calculate the density of the sugar water
                    density = total_sugar / total_water
                    
                    # Check if the density is greater than the current optimal solution
                    if density > optimal_solution[0]:
                        optimal_solution = [density, total_sugar]
    
    return optimal_solution

def main():
    a, b, c, d, e, f = map(int, input().split())
    print(*get_optimal_sugar_water(a, b, c, d, e, f))

if __name__ == '__main__':
    main()

