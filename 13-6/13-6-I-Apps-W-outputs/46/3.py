
def get_min_sum_square(numbers):
    # Sort the numbers in non-decreasing order
    numbers.sort()
    
    # Initialize the minimum sum of squares to a large value
    min_sum_square = float('inf')
    
    # Iterate over all possible group sizes
    for group_size in range(1, len(numbers) + 1):
        # Initialize the current sum of squares to 0
        current_sum_square = 0
        
        # Iterate over the groups
        for i in range(0, len(numbers), group_size):
            # Calculate the sum of the current group
            current_group_sum = sum(numbers[i:i + group_size])
            
            # Add the square of the current group sum to the current sum of squares
            current_sum_square += current_group_sum ** 2
        
        # If the current sum of squares is less than the minimum sum of squares, update the minimum sum of squares
        if current_sum_square < min_sum_square:
            min_sum_square = current_sum_square
    
    # Return the minimum sum of squares
    return min_sum_square

def main():
    # Read the input
    n = int(input())
    numbers = list(map(int, input().split()))
    
    # Calculate the minimum sum of squares
    min_sum_square = get_min_sum_square(numbers)
    
    # Print the result
    print(min_sum_square)

if __name__ == '__main__':
    main()

