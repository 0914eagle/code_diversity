
def find_player_with_box(starting_player, questions):
    player = starting_player
    for question in questions:
        if question[1] == "T":
            player = (player + 1) % 8
        elif question[1] == "N":
            return player
    return player

