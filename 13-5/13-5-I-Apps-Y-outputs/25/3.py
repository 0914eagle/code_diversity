
def find_player_with_box(initial_player, questions):
    player = initial_player
    for question in questions:
        if question[1] == "T":
            player = (player + 1) % 8
        elif question[1] == "N":
            return player
        else:
            return None
    return player

