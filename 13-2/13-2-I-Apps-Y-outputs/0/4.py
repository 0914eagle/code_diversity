
def is_sorted_string_possible(s):
    n = len(s)
    # Initialize the coloring as all zeros
    coloring = "0" * n
    # Loop through each character of the string
    for i in range(n):
        # If the current character is not in its correct position, i.e. it is not in alphabetical order,
        # then it is not possible to make the string sorted
        if s[i] != chr(ord('a') + i):
            return "NO"
    # If all characters are in their correct position, then it is possible to make the string sorted
    return "YES", coloring

