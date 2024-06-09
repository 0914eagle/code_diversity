
def is_sorted_string_possible(s):
    n = len(s)
    # Initialize the coloring as all characters being colored with the first color
    coloring = '0' * n
    # Loop through each character in the string
    for i in range(n):
        # If the current character is not the first character and is less than the previous character, it is impossible to sort the string
        if i > 0 and s[i] < s[i-1]:
            return "NO"
        # If the current character is not the first character and is equal to the previous character, flip the color of the previous character
        if i > 0 and s[i] == s[i-1]:
            coloring = coloring[:i-1] + '1' + coloring[i:]
    # If we reach this point, the string can be sorted, so return the coloring
    return "YES\n" + coloring

