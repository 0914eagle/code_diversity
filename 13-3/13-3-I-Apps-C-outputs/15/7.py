
def solve(a):
    # Convert the input to a string
    a_str = str(a)
    
    # Create a list to store the digits of a
    digits = []
    
    # Loop through each character in the string and append it to the list
    for char in a_str:
        digits.append(int(char))
    
    # Sort the list of digits in descending order
    digits.sort(reverse=True)
    
    # Create a new string to store the rearranged digits
    result = ""
    
    # Loop through the list of digits and append them to the result string
    for digit in digits:
        result += str(digit)
    
    # Convert the result string to an integer
    result = int(result)
    
    # Check if the result is divisible by 7
    if result % 7 == 0:
        return result
    else:
        return 0

