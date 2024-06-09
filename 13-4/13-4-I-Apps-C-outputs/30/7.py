
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
    
    # While the number of opening brackets is not equal to the number of closing brackets
    while opening_brackets != closing_brackets:
        # Find the longest substring of consecutive opening brackets
        start_index = 0
        end_index = 0
        for i in range(n):
            # If the current character is an opening bracket, set the start index to the current index
            if seq[i] == "(":
                start_index = i
            # If the current character is a closing bracket, set the end index to the current index
            elif seq[i] == ")":
                end_index = i
        
        # Reverse the substring
        seq = seq[:start_index] + seq[start_index:end_index+1][::-1] + seq[end_index+1:]
        
        # Increment the time by the length of the substring
        time += end_index - start_index + 1
        
        # Update the number of opening and closing brackets
        opening_brackets = seq.count("(")
        closing_brackets = seq.count(")")
    
    # Return the time
    return time

