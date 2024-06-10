
def get_player_with_box(initial_player, questions):
    player = initial_player
    for question in questions:
        if question[1] == "T":
            player = (player + 1) % 8
        elif question[1] == "N":
            return player
        else:
            return None
    return player

def main():
    initial_player = int(input())
    num_questions = int(input())
    questions = []
    for _ in range(num_questions):
        questions.append(list(map(int, input().split())))
    player_with_box = get_player_with_box(initial_player, questions)
    print(player_with_box)

if __name__ == '__main__':
    main()

