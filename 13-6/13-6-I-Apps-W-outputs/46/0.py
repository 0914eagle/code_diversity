
def get_optimal_solution(numbers):
    # Sort the numbers in non-decreasing order
    numbers.sort()
    
    # Initialize the minimum sum of squares to a large value
    min_sum_of_squares = float('inf')
    
    # Iterate over all possible group sizes
    for group_size in range(2, len(numbers) + 1):
        # Initialize the current sum of squares to 0
        current_sum_of_squares = 0
        
        # Iterate over the numbers in groups of size group_size
        for i in range(0, len(numbers), group_size):
            # Calculate the sum of the current group
            current_group_sum = sum(numbers[i:i+group_size])
            
            # Add the square of the current group sum to the current sum of squares
            current_sum_of_squares += current_group_sum ** 2
        
        # If the current sum of squares is less than the minimum sum of squares, update the minimum sum of squares
        if current_sum_of_squares < min_sum_of_squares:
            min_sum_of_squares = current_sum_of_squares
    
    # Return the minimum sum of squares
    return min_sum_of_squares

def main():
    # Read the input data
    n = int(input())
    numbers = list(map(int, input().split()))
    
    # Find the optimal solution
    optimal_solution = get_optimal_solution(numbers)
    
    # Print the optimal solution
    print(optimal_solution)

if __name__ == '__main__':
    main()

