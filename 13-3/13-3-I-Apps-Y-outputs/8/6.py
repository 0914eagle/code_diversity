
def is_postal_code(A, B, S):
    if len(S) != A + B + 1:
        return "No"
    if S[A] != "-":
        return "No"
    for i in range(A + 1, len(S)):
        if not S[i].isdigit():
            return "No"
    return "Yes"

