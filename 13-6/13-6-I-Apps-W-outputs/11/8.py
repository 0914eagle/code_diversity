
def solve(s):
    # Initialize variables
    k = 0
    n = len(s)
    palindrome = ""

    # While the length of the palindrome is less than the length of the original string
    while len(palindrome) < n:
        # If the palindrome is not empty and the first character is not the same as the last character
        if palindrome and palindrome[0] != palindrome[-1]:
            # Find the first occurrence of the first character that is not the same as the last character
            i = palindrome.find(palindrome[0])
            # If the first occurrence is not the last character
            if i != len(palindrome) - 1:
                # Append the substring from the first occurrence to the end of the palindrome
                palindrome += palindrome[i:]
                # Increment the number of operations
                k += 1
        # If the palindrome is empty or the first character is the same as the last character
        else:
            # Append the first character of the original string to the palindrome
            palindrome += s[0]

    # Return the number of operations and the palindrome
    return k, palindrome

