
def solve(gunnar_dice, emma_dice):
    gunnar_sum = sum([(b-a+1) for a, b in gunnar_dice])
    emma_sum = sum([(b-a+1) for a, b in emma_dice])
    if gunnar_sum > emma_sum:
        return "Gunnar"
    elif gunnar_sum < emma_sum:
        return "Emma"
    else:
        return "Tie"

