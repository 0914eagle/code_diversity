
def solve(s):
    # Initialize variables
    max_length = 0
    start_index = 0
    end_index = 0

    # Iterate through the string
    for i in range(len(s)):
        # Check if the current character is 'A'
        if s[i] == 'A':
            # If it is, set the start index to the current index
            start_index = i

        # Check if the current character is 'Z'
        if s[i] == 'Z':
            # If it is, set the end index to the current index
            end_index = i

            # Check if the length of the substring is greater than the maximum length
            if end_index - start_index + 1 > max_length:
                # If it is, update the maximum length
                max_length = end_index - start_index + 1

    # Return the maximum length
    return max_length

