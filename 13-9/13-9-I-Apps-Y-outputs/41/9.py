
def solve(gunnars_dice, emmas_dice):
    gunnars_sum = sum(range(gunnars_dice[0], gunnars_dice[1] + 1))
    emmas_sum = sum(range(emmas_dice[0], emmas_dice[1] + 1))
    if gunnars_sum > emmas_sum:
        return "Gunnar"
    elif gunnars_sum < emmas_sum:
        return "Emma"
    else:
        return "Tie"

