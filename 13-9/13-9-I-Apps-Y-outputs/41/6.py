
def solve(gunnar_dice, emma_dice):
    gunnar_sum = 0
    emma_sum = 0
    for die in gunnar_dice:
        gunnar_sum += die[1] - die[0] + 1
    for die in emma_dice:
        emma_sum += die[1] - die[0] + 1
    if gunnar_sum > emma_sum:
        return "Gunnar"
    elif gunnar_sum < emma_sum:
        return "Emma"
    else:
        return "Tie"

