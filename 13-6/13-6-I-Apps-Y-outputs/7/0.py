
def solve(n, k, d, s):
    if k == 0:
        return "impossible"
    total_difficulty = d * k
    team_difficulty = s * k
    unsolved_difficulty = total_difficulty - team_difficulty
    return unsolved_difficulty / (n - k)

