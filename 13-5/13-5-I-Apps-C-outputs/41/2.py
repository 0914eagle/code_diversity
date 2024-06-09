
def solve(a, b, c, d):
    # Convert the input to a list of integers
    input_list = [a, b, c, d]
    
    # Initialize an empty string
    string = ""
    
    # Loop through the input list and append the corresponding binary digit to the string
    for i in input_list:
        if i % 2 == 0:
            string += "0"
        else:
            string += "1"
    
    # Return the string
    return string

