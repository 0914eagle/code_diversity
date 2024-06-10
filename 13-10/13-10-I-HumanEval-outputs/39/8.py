
def is_equal_to_sum_even(n: int) -> bool:
    
    # Initialize a list to store the numbers
    numbers = []
    # Initialize a variable to keep track of the sum
    sum = 0
    # Iterate until the sum is equal to n
    while sum < n:
        # Append a positive even number to the list
        numbers.append(2 * (len(numbers) + 1))
        # Update the sum
        sum += numbers[-1]
    # Check if the sum is equal to n
    return sum == n

