
def solve(a, b, c, d):
    # Convert the input to a list of lists
    input_list = [[a, 0], [b, 1], [c, 2], [d, 3]]
    
    # Sort the list by the first element of each sublist (i.e., the frequency) in descending order
    input_list.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize the output string
    output_string = ""
    
    # Loop through the input list and append the corresponding binary digit to the output string
    for freq, digit in input_list:
        output_string += str(digit)
    
    # Return the output string if it has the required properties, otherwise return "impossible"
    if is_valid_string(output_string, a, b, c, d):
        return output_string
    else:
        return "impossible"

# Check if the output string has the required properties
def is_valid_string(output_string, a, b, c, d):
    # Count the number of occurrences of each subsequence in the output string
    subsequence_counts = [output_string.count(str(i)) for i in range(4)]
    
    # Check if the subsequence counts match the input frequencies
    return subsequence_counts == [a, b, c, d]

