
def check_doublets(dice_rolls):
    for i in range(len(dice_rolls) - 2):
        if dice_rolls[i][0] == dice_rolls[i][1] and dice_rolls[i+1][0] == dice_rolls[i+1][1] and dice_rolls[i+2][0] == dice_rolls[i+2][1]:
            return "Yes"
    return "No"

