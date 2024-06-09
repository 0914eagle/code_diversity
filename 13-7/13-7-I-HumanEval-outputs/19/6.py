
def is_equal_to_sum_even(n: int) -> bool:
    
    # Initialize a counter for the number of even numbers
    count = 0
    # Iterate through the numbers from 1 to n
    for i in range(1, n + 1):
        # Check if the current number is even
        if i % 2 == 0:
            # Increment the counter
            count += 1
            # Check if the current number is equal to n
            if i == n:
                # If the current number is equal to n, return True
                return True
    # If the counter is equal to 4, return True
    return count == 4

