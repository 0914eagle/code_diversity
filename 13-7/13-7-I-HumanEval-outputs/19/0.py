
def is_equal_to_sum_even(n: int) -> bool:
    
    # Initialize a list to store the even numbers
    even_numbers = []
    
    # Iterate from 1 to n
    for i in range(1, n+1):
        # Check if the current number is even
        if i % 2 == 0:
            # Add the current number to the list of even numbers
            even_numbers.append(i)
    
    # Check if the sum of the even numbers is equal to n
    return sum(even_numbers) == n

