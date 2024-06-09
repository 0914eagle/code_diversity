
def solve(k):
    # Initialize variables
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    min_length = 1000
    min_string = ''

    # Iterate through all possible strings
    for i in range(len(alphabet)):
        for j in range(i+1, len(alphabet)):
            # Calculate the sum of the absolute differences between consecutive letters
            sum_abs_diff = abs(alphabet[i] - alphabet[j])
            for k in range(j+1, len(alphabet)):
                sum_abs_diff += abs(alphabet[j] - alphabet[k])

            # If the sum of absolute differences is equal to the input number, return the string
            if sum_abs_diff == k:
                return alphabet[i] + alphabet[j] + alphabet[k]

            # If the sum of absolute differences is less than the minimum length, update the minimum length and the minimum string
            if sum_abs_diff < min_length:
                min_length = sum_abs_diff
                min_string = alphabet[i] + alphabet[j] + alphabet[k]

    # Return the minimum string if no string is found with the exact sum
    return min_string

