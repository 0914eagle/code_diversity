
def is_hard_to_enter(S):
    return "Bad" if any(S[i] == S[i+1] for i in range(len(S)-1)) else "Good"

