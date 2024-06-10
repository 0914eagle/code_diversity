
def get_next_player(current_player, answer, time_passed):
    if answer == "T":
        return (current_player + 1) % 8
    else:
        return current_player

def get_player_with_box(time_passed, answers):
    current_player = 1
    for i in range(len(answers)):
        answer = answers[i]
        time_passed -= int(answer[0])
        current_player = get_next_player(current_player, answer[1], time_passed)
        if time_passed <= 0:
            break
    return current_player

def main():
    k, n = map(int, input().split())
    answers = [input().split() for _ in range(n)]
    time_passed = 3 * 60 + 30
    player_with_box = get_player_with_box(time_passed, answers)
    print(player_with_box)

if __name__ == '__main__':
    main()

