
def get_player_with_box(initial_player, questions):
    player = initial_player
    for question in questions:
        if question[1] == "T":
            player = (player + 1) % 8
        elif question[1] == "N":
            return player
    return player

def get_player_with_box_after_explosion(initial_player, questions):
    player = initial_player
    for question in questions:
        if question[1] == "T":
            player = (player + 1) % 8
        elif question[1] == "N":
            return player
    return (player + 1) % 8

if __name__ == '__main__':
    initial_player = int(input())
    num_questions = int(input())
    questions = []
    for i in range(num_questions):
        questions.append([int(input()), input()])
    print(get_player_with_box(initial_player, questions))
    print(get_player_with_box_after_explosion(initial_player, questions))

