
def get_palindromic_strings(strings):
    # Initialize a list to store the palindromic strings
    palindromic_strings = []

    # Loop through each string in the input list
    for string in strings:
        # Check if the string is already palindromic
        if string == string[::-1]:
            # If it is, add it to the list of palindromic strings
            palindromic_strings.append(string)

    # Return the list of palindromic strings
    return palindromic_strings

