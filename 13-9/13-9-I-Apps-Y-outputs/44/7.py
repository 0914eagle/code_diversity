
def is_hard_to_enter(S):
    # Check if the second and third digits are the same
    if S[1] == S[2]:
        return "Bad"
    else:
        return "Good"

