
def solve(s):
    if s[0] == "A" and s[2] == "B":
        return "Yes"
    elif s[0] == "B" and s[2] == "A":
        return "Yes"
    else:
        return "No"

