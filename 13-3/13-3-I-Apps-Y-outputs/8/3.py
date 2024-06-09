
def is_postal_code(s):
    A, B = map(int, input().split())
    if len(s) != A + B + 1:
        return "No"
    if s[A] != "-":
        return "No"
    if not s[A+1:].isdigit():
        return "No"
    return "Yes"

