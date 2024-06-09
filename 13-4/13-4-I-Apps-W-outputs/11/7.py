
def is_telephone_number(s):
    if len(s) != 11:
        return "NO"
    if s[0] != "8":
        return "NO"
    if any(s[i] != "8" for i in range(1, 11, 2)):
        return "NO"
    return "YES"

