
def get_winner(gunnar_dice, emma_dice):
    gunnar_sum = sum(range(gunnar_dice[0], gunnar_dice[1] + 1))
    emma_sum = sum(range(emma_dice[0], emma_dice[1] + 1))
    if gunnar_sum > emma_sum:
        return "Gunnar"
    elif gunnar_sum < emma_sum:
        return "Emma"
    else:
        return "Tie"

