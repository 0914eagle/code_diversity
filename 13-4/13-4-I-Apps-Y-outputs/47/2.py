
def solve(a1, b1, a2, b2):
    sum1 = (b1 - a1 + 1) + (b1 - a1 + 2)
    sum2 = (b2 - a2 + 1) + (b2 - a2 + 2)
    if sum1 > sum2:
        return "Gunnar"
    elif sum1 < sum2:
        return "Emma"
    else:
        return "Tie"

