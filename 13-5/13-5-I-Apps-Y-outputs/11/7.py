
def solve(N, dice_rolls):
    for i in range(N-2):
        if dice_rolls[i] == dice_rolls[i+1] == dice_rolls[i+2]:
            return "Yes"
    return "No"

