
def is_telephone_number(s):
    if len(s) != 11:
        return "NO"
    if s[0] != "8":
        return "NO"
    if any(c not in "0123456789" for c in s):
        return "NO"
    return "YES"

