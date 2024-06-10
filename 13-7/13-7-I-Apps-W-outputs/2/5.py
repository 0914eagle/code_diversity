
def get_num_players_can_show_hands(statuses):
    num_players_can_show_hands = 0
    for i in range(len(statuses)):
        if statuses[i] == "A" or statuses[i] == "F":
            num_players_can_show_hands += 1
    return num_players_can_show_hands

def get_num_players_cant_show_hands(statuses):
    num_players_cant_show_hands = 0
    for i in range(len(statuses)):
        if statuses[i] == "I":
            num_players_cant_show_hands += 1
    return num_players_cant_show_hands

def main():
    num_players = int(input())
    statuses = input()
    num_players_can_show_hands = get_num_players_can_show_hands(statuses)
    num_players_cant_show_hands = get_num_players_cant_show_hands(statuses)
    print(num_players_can_show_hands + num_players_cant_show_hands)

if __name__ == '__main__':
    main()

