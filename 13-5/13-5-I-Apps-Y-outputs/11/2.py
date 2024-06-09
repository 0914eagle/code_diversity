
def solve(N, dice):
    for i in range(N-2):
        if dice[i] == dice[i+1] and dice[i+1] == dice[i+2]:
            return "Yes"
    return "No"

