
def find_beautiful_number(p, x):
    # Initialize a list to store the possible numbers
    numbers = []
    
    # Loop through all possible numbers with p decimal digits
    for i in range(10**p):
        # Convert the number to a string
        num_str = str(i)
        
        # Check if the number has no leading zeroes
        if num_str.startswith("0"):
            continue
        
        # Check if the number has the correct length
        if len(num_str) != p:
            continue
        
        # Check if the number grows correctly when the last digit is moved to the beginning
        if int(num_str[-1]) * x != int(num_str[1:] + num_str[0]):
            continue
        
        # Add the number to the list of possible numbers
        numbers.append(num_str)
    
    # Check if any numbers were found
    if not numbers:
        return "Impossible"
    
    # Return the smallest number in the list of possible numbers
    return min(numbers)

