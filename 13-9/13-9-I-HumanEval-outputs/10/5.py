
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
                # If the current number is equal to n, return True if the counter is 4
                return count == 4
    # If the loop completes and the counter is not 4, return False
    return False

