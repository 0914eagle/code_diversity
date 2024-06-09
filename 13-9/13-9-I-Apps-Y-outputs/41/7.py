
def get_winner(gunnar_dice, emma_dice):
    gunnar_sum = sum(gunnar_dice)
    emma_sum = sum(emma_dice)
    if gunnar_sum > emma_sum:
        return "Gunnar"
    elif gunnar_sum < emma_sum:
        return "Emma"
    else:
        return "Tie"

