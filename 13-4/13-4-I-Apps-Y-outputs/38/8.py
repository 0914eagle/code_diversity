
def solve(s):
    # Initialize variables
    start_index = 0
    end_index = 0
    max_length = 0

    # Iterate through the string
    for i in range(len(s)):
        # Check if the current character is 'A'
        if s[i] == 'A':
            # If so, set the start index to the current index
            start_index = i

        # Check if the current character is 'Z'
        if s[i] == 'Z':
            # If so, set the end index to the current index
            end_index = i

            # Check if the length of the substring is greater than the maximum length
            if end_index - start_index + 1 > max_length:
                # If so, update the maximum length
                max_length = end_index - start_index + 1

    # Return the maximum length
    return max_length

