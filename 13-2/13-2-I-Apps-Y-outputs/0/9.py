
def is_sorted_string_possible(s):
    n = len(s)
    # Initialize the coloring as all characters being colored with the first color
    coloring = "0" * n
    # Loop through each character in the string
    for i in range(n):
        # If the current character is not the smallest character in the string,
        # and it is colored with the first color,
        # and the previous character is not the smallest character in the string,
        # and it is colored with the second color,
        # then it is not possible to make the string sorted
        if s[i] != min(s) and coloring[i] == "0" and s[i-1] != min(s) and coloring[i-1] == "1":
            return "NO"
    return "YES"

