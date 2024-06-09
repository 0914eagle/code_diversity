
def get_palindromic_strings(strings):
    # Initialize a list to store the indices of palindromic strings
    palindromic_strings = []

    # Loop through each string in the input list
    for i, string in enumerate(strings):
        # Check if the string is already palindromic
        if string == string[::-1]:
            # If it is, add its index to the list of palindromic strings
            palindromic_strings.append(i)

    # Return the list of palindromic strings
    return palindromic_strings

