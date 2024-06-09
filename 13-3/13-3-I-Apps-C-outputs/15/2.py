
def solve(a):
    # Convert the input to a string
    a_str = str(a)
    
    # Create a list to store the digits of a
    a_list = []
    
    # Iterate through the string and append the digits to the list
    for char in a_str:
        if char.isdigit():
            a_list.append(int(char))
    
    # Sort the list in descending order
    a_list.sort(reverse=True)
    
    # Create a new string from the sorted list
    result = ""
    for digit in a_list:
        result += str(digit)
    
    # Check if the result is divisible by 7
    if int(result) % 7 == 0:
        return result
    else:
        return "0"

