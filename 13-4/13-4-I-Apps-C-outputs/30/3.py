
def solve(n, seq):
    # Initialize variables
    opening_brackets = 0
    closing_brackets = 0
    time = 0

    # Iterate through the sequence
    for i in range(n):
        # If the current character is an opening bracket, increment the opening bracket count
        if seq[i] == "(":
            opening_brackets += 1
        # If the current character is a closing bracket, increment the closing bracket count
        elif seq[i] == ")":
            closing_brackets += 1

    # If the number of opening brackets is not equal to the number of closing brackets, return -1
    if opening_brackets != closing_brackets:
        return -1

    # Iterate through the sequence again
    for i in range(n):
        # If the current character is an opening bracket, increment the time by 1
        if seq[i] == "(":
            time += 1
        # If the current character is a closing bracket, decrement the time by 1
        elif seq[i] == ")":
            time -= 1

    # Return the minimum time required to make the sequence correct
    return time

