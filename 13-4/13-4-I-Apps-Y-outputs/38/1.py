
def solve(s):
    # Initialize variables
    max_length = 0
    start_index = 0
    end_index = 0

    # Iterate through the string
    for i in range(len(s)):
        # Check if the substring starting at index i ends with Z
        if s[i] == "Z":
            # Check if the substring starting at index 0 and ending at index i-1 starts with A
            if s[0] == "A":
                # Update the maximum length and indices
                max_length = i - start_index + 1
                start_index = 0
                end_index = i

    # Return the maximum length
    return max_length

