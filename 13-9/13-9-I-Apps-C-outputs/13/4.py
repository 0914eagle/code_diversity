
import itertools

def is_valid_play(play):
    
    return play in ["A", "2", "3", "4", "5", "T"]

def get_next_play(play):
    
    if play == "A":
        return "2"
    elif play == "2":
        return "3"
    elif play == "3":
        return "4"
    elif play == "4":
        return "5"
    elif play == "5":
        return "T"
    else:
        return "A"

def get_winner(player_1, player_2):
    
    player_1_wins = 0
    player_2_wins = 0
    for i in range(10):
        if player_1[i] == get_next_play(player_2[i]):
            player_1_wins += 1
        elif player_2[i] == get_next_play(player_1[i]):
            player_2_wins += 1
    if player_1_wins == 10:
        return "Theta wins"
    elif player_2_wins == 10:
        return "Theta loses"
    else:
        return "Draw"

def get_player_hands(deck):
    
    player_1 = deck[:10]
    player_2 = deck[10:]
    return player_1, player_2

def get_shuffled_deck():
    
    deck = list(itertools.chain.from_iterable(itertools.product(["A", "2", "3", "4", "5", "T"], ["S", "H", "D", "C"])))
    return deck

def main():
    deck = get_shuffled_deck()
    player_1, player_2 = get_player_hands(deck)
    print(get_winner(player_1, player_2))

if __name__ == '__main__':
    main()

