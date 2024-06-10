
def get_num_players_can_show_hands(statuses):
    num_players_can_show_hands = 0
    for i in range(len(statuses)):
        if statuses[i] != "F" and (i == 0 or statuses[i-1] in ["F", "A"]):
            num_players_can_show_hands += 1
    return num_players_can_show_hands

def main():
    num_players = int(input())
    statuses = input()
    print(get_num_players_can_show_hands(statuses))

if __name__ == '__main__':
    main()

