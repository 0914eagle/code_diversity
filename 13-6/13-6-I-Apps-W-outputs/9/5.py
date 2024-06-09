
def get_max_sum(numbers):
    # Calculate the sum of the given numbers
    sum_numbers = sum(numbers)
    
    # Initialize the maximum sum to the current sum
    max_sum = sum_numbers
    
    # Iterate over the numbers
    for i in range(len(numbers)):
        # Calculate the sum of the numbers after multiplying the current number by -1
        sum_negative = sum_numbers - numbers[i]
        
        # If the sum of the negative numbers is greater than the maximum sum, update the maximum sum
        if sum_negative > max_sum:
            max_sum = sum_negative
    
    return max_sum

def main():
    # Read the input from stdin
    n = int(input())
    numbers = list(map(int, input().split()))
    
    # Call the get_max_sum function and print the result
    print(get_max_sum(numbers))

if __name__ == '__main__':
    main()

