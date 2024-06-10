
def get_current_player(starting_player, time_passed, answers):
    current_player = starting_player
    for i in range(len(answers)):
        if answers[i] == "T":
            current_player = (current_player + 1) % 8
        elif answers[i] == "N":
            current_player = (current_player + 2) % 8
        elif answers[i] == "P":
            current_player = (current_player + 3) % 8
        time_passed -= 30
    return current_player

def get_final_player(starting_player, answers):
    current_player = starting_player
    for i in range(len(answers)):
        if answers[i] == "T":
            current_player = (current_player + 1) % 8
        elif answers[i] == "N":
            current_player = (current_player + 2) % 8
        elif answers[i] == "P":
            current_player = (current_player + 3) % 8
    return current_player

def main():
    starting_player = int(input())
    num_questions = int(input())
    answers = []
    for i in range(num_questions):
        time_passed, answer = map(str, input().split())
        answers.append(answer)
    final_player = get_final_player(starting_player, answers)
    print(final_player)

if __name__ == '__main__':
    main()

