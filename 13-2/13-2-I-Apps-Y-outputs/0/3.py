
def is_sorted_string_possible(s):
    n = len(s)
    # Initialize the coloring as all characters being colored with the first color
    coloring = '0' * n
    # Loop through each character in the string
    for i in range(n):
        # If the current character is not already in its correct position
        if s[i] != chr(ord('a') + i):
            # Find the correct position of the current character
            correct_pos = ord(s[i]) - ord('a')
            # If the correct position is not the current position and the characters at the correct position and the current position have different colors
            if correct_pos != i and coloring[correct_pos] == coloring[i]:
                # It is not possible to make the string sorted
                return "NO"
            # Swap the characters at the correct position and the current position
            coloring = coloring[:correct_pos] + coloring[i] + coloring[correct_pos + 1:i] + coloring[i + 1:]
    # It is possible to make the string sorted
    return "YES", coloring

