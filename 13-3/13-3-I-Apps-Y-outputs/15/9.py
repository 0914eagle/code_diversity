
def f1(S):
    # Initialize the minimum difference and the corresponding substring
    min_diff = float('inf')
    substring = ''

    # Iterate over all possible substrings of length 3
    for i in range(len(S) - 2):
        # Extract the substring and convert it to an integer
        substring = S[i:i+3]
        x = int(substring)

        # Calculate the absolute difference between x and 753
        diff = abs(x - 753)

        # Update the minimum difference and the corresponding substring
        if diff < min_diff:
            min_diff = diff
            substring = substring

    # Return the minimum difference and the corresponding substring
    return min_diff, substring

