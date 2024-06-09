
def solve(strings):
    n = len(strings)
    if n == 1:
        return "YES\n" + strings[0]

    # sort the strings in decreasing order of length
    sorted_strings = sorted(strings, key=len, reverse=True)

    # create a list to store the reordered strings
    reordered_strings = []

    # iterate through the sorted strings and check if they are substrings of the previous strings
    for i in range(n):
        current_string = sorted_strings[i]
        is_substring = False
        for j in range(i):
            if current_string in reordered_strings[j]:
                is_substring = True
                break
        if not is_substring:
            return "NO"
        reordered_strings.append(current_string)

    return "YES\n" + "\n".join(reordered_strings)

