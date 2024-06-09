
def solve(box_player, questions):
    player = box_player
    for time, answer in questions:
        if answer == "T":
            player = (player + 1) % 8
        elif answer == "N":
            return player
    return player

