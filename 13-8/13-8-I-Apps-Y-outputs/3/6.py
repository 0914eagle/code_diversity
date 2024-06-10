
def find_player_with_box(initial_player, questions):
    player = initial_player
    for time, answer in questions:
        if answer == "T":
            player = (player + 1) % 8
        elif answer == "P":
            return player
    return player

def main():
    initial_player = int(input())
    num_questions = int(input())
    questions = []
    for _ in range(num_questions):
        time, answer = input().split()
        questions.append((int(time), answer))
    print(find_player_with_box(initial_player, questions))

if __name__ == '__main__':
    main()

