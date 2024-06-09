
def solve(s):
    # Initialize variables
    k = 0
    n = len(s)
    result = s

    # Loop until the string is a palindrome or the maximum number of operations is reached
    while k < 30 and result != result[::-1]:
        # Check if the string can be made a palindrome by appending the reverse of the substring starting at index 2
        if s[2:] == s[2:][::-1]:
            result = "L " + str(2) + "\n" + result
            k += 1
        # Check if the string can be made a palindrome by appending the reverse of the substring ending at index n-1
        elif s[:n-1] == s[:n-1][::-1]:
            result = "R " + str(n-1) + "\n" + result
            k += 1
        # If neither of the above conditions are met, return "Impossible"
        else:
            return "Impossible"

    # Return the result
    return str(k) + "\n" + result

