
def solve(D, T, S):
    time_to_reach = D / S
    if time_to_reach <= T:
        return "Yes"
    else:
        return "No"

