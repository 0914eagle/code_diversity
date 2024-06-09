
def is_sorted_string_coloring_possible(s):
    n = len(s)
    # Initialize the coloring as all characters are colored with the first color
    coloring = '0' * n
    # Loop through each character of the string
    for i in range(n):
        # If the current character is not the smallest character in the string,
        # and it is colored with the first color,
        # and the previous character is not the smallest character in the string,
        # and it is colored with the second color,
        # then it is not possible to make the string sorted by coloring and swapping
        if s[i] != min(s) and coloring[i] == '0' and s[i-1] != min(s) and coloring[i-1] == '1':
            return "NO"
    return "YES"

