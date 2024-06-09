
def get_dog_name(n):
    # Convert the input to string
    n = str(n)
    
    # Initialize an empty string to store the name
    name = ""
    
    # Loop through each digit of the input
    for digit in n:
        # Convert the digit to its corresponding letter
        letter = chr(ord('a') + int(digit) - 1)
        # Add the letter to the name
        name += letter
    
    # Return the name
    return name

