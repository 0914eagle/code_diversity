
def is_postal_code(S):
    A, B = map(int, input().split())
    if len(S) != A + B + 1:
        return "No"
    if S[A] != "-":
        return "No"
    if not S[A+1:].isdigit():
        return "No"
    return "Yes"

