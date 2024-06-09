
def is_coffee_like(s):
    if len(s) != 6:
        return "No"
    if s[2] != s[3]:
        return "No"
    if s[4] != s[5]:
        return "No"
    return "Yes"

