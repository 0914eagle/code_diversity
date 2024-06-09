
def solve(D, T, S):
    time_to_travel = D / S
    if time_to_travel <= T:
        return "Yes"
    else:
        return "No"

