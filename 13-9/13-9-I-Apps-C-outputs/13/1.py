
import itertools

def get_deck_combinations(deck):
    
    return itertools.permutations(deck)

def get_winning_combination(deck, player_cards, friend_cards):
    
    combinations = get_deck_combinations(deck)
    for combination in combinations:
        player_cards_copy = player_cards[:]
        friend_cards_copy = friend_cards[:]
        for card in combination:
            if card in player_cards_copy:
                player_cards_copy.remove(card)
            elif card in friend_cards_copy:
                friend_cards_copy.remove(card)
        if not player_cards_copy and not friend_cards_copy:
            return combination
    return None

def get_jack_combination(deck, player_cards, friend_cards):
    
    combinations = get_deck_combinations(deck)
    for combination in combinations:
        player_cards_copy = player_cards[:]
        friend_cards_copy = friend_cards[:]
        for card in combination:
            if card in player_cards_copy:
                player_cards_copy.remove(card)
            elif card in friend_cards_copy:
                friend_cards_copy.remove(card)
        if card == 'J' and not player_cards_copy and not friend_cards_copy:
            return combination
    return None

def get_player_cards(deck, player_cards):
    
    player_cards_copy = player_cards[:]
    for card in deck:
        if card in player_cards_copy:
            player_cards_copy.remove(card)
    return player_cards_copy

def get_friend_cards(deck, friend_cards):
    
    friend_cards_copy = friend_cards[:]
    for card in deck:
        if card in friend_cards_copy:
            friend_cards_copy.remove(card)
    return friend_cards_copy

def get_winner(deck, player_cards, friend_cards):
    
    player_cards_copy = get_player_cards(deck, player_cards)
    friend_cards_copy = get_friend_cards(deck, friend_cards)
    if not player_cards_copy and not friend_cards_copy:
        return "Theta wins"
    winning_combination = get_winning_combination(deck, player_cards_copy, friend_cards_copy)
    if winning_combination:
        return "Theta wins"
    jack_combination = get_jack_combination(deck, player_cards_copy, friend_cards_copy)
    if jack_combination:
        return "Theta wins"
    return "Theta loses"

def main():
    deck = input()
    deck = deck.split()
    player_cards = deck[:10]
    friend_cards = deck[10:]
    print(get_winner(deck, player_cards, friend_cards))

if __name__ == '__main__':
    main()

