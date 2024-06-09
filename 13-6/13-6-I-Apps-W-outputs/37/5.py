
def solve(s):
    # Check if the string is empty
    if not s:
        return "NET"

    # Check if the string has only one character
    if len(s) == 1:
        return "DA"

    # Check if the string has only two characters and they are the same
    if len(s) == 2 and s[0] == s[1]:
        return "NET"

    # Check if the string has only two characters and they are different
    if len(s) == 2 and s[0] != s[1]:
        return "DA"

    # Check if the string has more than two characters
    if len(s) > 2:
        # Check if the first and last characters are the same
        if s[0] == s[-1]:
            # Check if the second and second-to-last characters are the same
            if s[1] == s[-2]:
                return "DA"
            else:
                return "NET"
        else:
            # Check if the second and second-to-last characters are the same
            if s[1] == s[-2]:
                return "NET"
            else:
                return "DA"

    return "NET"

