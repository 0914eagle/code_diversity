
def get_player_with_box(initial_player, questions):
    player = initial_player
    for time, answer in questions:
        if answer == "T":
            player = (player + 1) % 8
        elif answer == "P":
            break
    return player

def get_player_with_box_after_explosion(initial_player, questions):
    player = initial_player
    for time, answer in questions:
        if answer == "T":
            player = (player + 1) % 8
        elif answer == "P":
            break
    return (player + 1) % 8

if __name__ == '__main__':
    initial_player = int(input())
    num_questions = int(input())
    questions = []
    for i in range(num_questions):
        time, answer = input().split()
        questions.append((int(time), answer))
    print(get_player_with_box(initial_player, questions))
    print(get_player_with_box_after_explosion(initial_player, questions))

