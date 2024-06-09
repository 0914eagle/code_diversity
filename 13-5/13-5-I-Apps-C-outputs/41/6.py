
def solve(a, b, c, d):
    # Convert the input to a list of lists
    input_list = [[a, 0], [b, 1], [c, 2], [d, 3]]
    
    # Sort the list by the first element in each sublist (i.e., the number of occurrences)
    input_list.sort(key=lambda x: x[0])
    
    # Initialize the output string
    output_string = ""
    
    # Iterate through the list and append the corresponding binary digit to the output string
    for sublist in input_list:
        output_string += str(sublist[1])
    
    return output_string

