
def check_security_code(S):
    if len(S) != 4:
        return "Bad"
    if S[1] == S[2] or S[2] == S[3]:
        return "Bad"
    return "Good"

