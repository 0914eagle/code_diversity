
def solve(a, b, c, d):
    # Check if the given integers satisfy the required conditions
    if a + b + c + d != 4:
        return "impossible"
    
    # Initialize an empty string
    string = ""
    
    # Add characters to the string to satisfy the required subsequence occurrences
    for i in range(a):
        string += "00"
    for i in range(b):
        string += "01"
    for i in range(c):
        string += "10"
    for i in range(d):
        string += "11"
    
    # Return the final string
    return string

