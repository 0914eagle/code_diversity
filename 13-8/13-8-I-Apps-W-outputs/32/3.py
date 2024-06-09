
def get_non_palindromic_string(n):
    
    if n == 1:
        return "a"
    if n == 2:
        return "aa"
    if n == 3:
        return "bba"
    # Initialize the string with 'a's
    string = "a" * (n - 1)
    # Add the final letter
    string += "b"
    # Iterate through the string and check for palindromes
    for i in range(n - 3):
        if string[i] == string[i + 1] and string[i + 1] == string[i + 2]:
            string = string[:i] + "b" + string[i + 1:]
    return string

