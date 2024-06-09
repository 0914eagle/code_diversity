
def solve(s):
    # Check if there are two stations with different companies
    if s[0] != s[2] and s[1] != s[0] and s[1] != s[2]:
        return "Yes"
    else:
        return "No"

