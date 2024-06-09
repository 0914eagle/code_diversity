
def is_hard_to_enter(S):
    if S[1] == S[2] or S[2] == S[3]:
        return "Bad"
    return "Good"

