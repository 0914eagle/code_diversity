
def solve(strings):
    n = len(strings)
    if n == 1:
        return "YES\n" + strings[0]

    # sort the strings in decreasing order of length
    strings.sort(key=len, reverse=True)

    # create a list to store the ordered strings
    ordered_strings = []

    # iterate through the strings and check if they are substrings of the previous strings
    for i in range(n):
        is_substring = False
        for j in range(i):
            if strings[i] in ordered_strings[j]:
                is_substring = True
                break
        if not is_substring:
            return "NO"
        ordered_strings.append(strings[i])

    return "YES\n" + "\n".join(ordered_strings)

