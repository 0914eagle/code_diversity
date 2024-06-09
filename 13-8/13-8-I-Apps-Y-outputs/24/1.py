
def solve(S_A, S_B, S_C):
    while S_A or S_B or S_C:
        if S_A:
            S_A = S_A[1:]
            if S_A:
                next_player = S_A[0]
            else:
                return "A"
        elif S_B:
            S_B = S_B[1:]
            if S_B:
                next_player = S_B[0]
            else:
                return "B"
        else:
            S_C = S_C[1:]
            if S_C:
                next_player = S_C[0]
            else:
                return "C"
        if next_player == "a":
            S_A = S_A[1:]
        elif next_player == "b":
            S_B = S_B[1:]
        else:
            S_C = S_C[1:]
    return "D"

