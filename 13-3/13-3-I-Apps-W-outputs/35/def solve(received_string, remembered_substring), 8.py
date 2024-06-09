
def solve(received_string, remembered_substring):
    # Initialize a set to store all possible numbers
    numbers = set()
    
    # Iterate through all possible numbers
    for i in range(1000000):
        # Convert the number to a string
        number_string = str(i)
        
        # Check if the number string contains the remembered substring
        if remembered_substring in number_string:
            # Add the number to the set
            numbers.add(i)
    
    # Sort the set in ascending order
    sorted_numbers = sorted(numbers)
    
    # Return the smallest number in the set
    return sorted_numbers[0]

