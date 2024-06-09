
def get_winner(gunnars_dice, emmas_dice):
    gunnars_sum = sum(gunnars_dice)
    emmas_sum = sum(emmas_dice)
    if gunnars_sum > emmas_sum:
        return "Gunnar"
    elif gunnars_sum < emmas_sum:
        return "Emma"
    else:
        return "Tie"

