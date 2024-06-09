
def find_player_with_box(initial_player, questions):
    player = initial_player
    for time, answer in questions:
        if answer == "T":
            player = (player + 1) % 8
        elif answer == "N":
            return player
    return player

