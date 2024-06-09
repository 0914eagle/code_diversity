
def solve(n, k):
    # Initialize an empty string
    s = ""
    # Loop through each letter of the alphabet
    for i in range(1, 27):
        # If the letter is in the string, add it to the end
        if str(i) in s:
            s += str(i)
        # If the letter is not in the string and there are still letters left to add, add it to the end
        elif len(s) < n:
            s += str(i)
    # Return the string
    return s

