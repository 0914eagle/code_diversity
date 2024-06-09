
def find_winner(dice1, dice2):
    sum1 = sum([i for i in range(dice1[0], dice1[1]+1)])
    sum2 = sum([i for i in range(dice2[0], dice2[1]+1)])
    if sum1 > sum2:
        return "Gunnar"
    elif sum1 < sum2:
        return "Emma"
    else:
        return "Tie"

