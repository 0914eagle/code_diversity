
def get_min_sum_squares(numbers):
    # Sort the numbers in non-decreasing order
    numbers.sort()
    
    # Initialize the minimum sum of squares to a large value
    min_sum_squares = float('inf')
    
    # Iterate over all possible combinations of numbers
    for i in range(1, len(numbers)):
        for j in range(0, len(numbers) - i + 1):
            # Calculate the sum of the current combination
            current_sum = sum(numbers[j:j+i])
            
            # Calculate the sum of the squares of the current combination
            current_sum_squares = sum([x**2 for x in numbers[j:j+i]])
            
            # Update the minimum sum of squares if necessary
            if current_sum_squares < min_sum_squares:
                min_sum_squares = current_sum_squares
    
    return min_sum_squares

def main():
    # Read the input data
    n = int(input())
    numbers = [int(x) for x in input().split()]
    
    # Calculate the minimum sum of squares
    min_sum_squares = get_min_sum_squares(numbers)
    
    # Print the result
    print(min_sum_squares)

if __name__ == '__main__':
    main()

