ialize_deck():
    deck = ['A', 'A', 'A', 'A', 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K']
    for i in range(2, 10):
        deck.extend([str(i)] * 4)
    return deck

def deal_cards(deck):
    theta_hand = deck[:10]
    friend_hand = deck[10:20]
    drawing_pile = deck[20:]
    return theta_hand, friend_hand, drawing_pile

def play_game(deck):
    theta_hand, friend_hand, drawing_pile = deal_cards(deck)
    theta_slots = [[], []]
    friend_slots = [[], []]
    current_player = 'Theta'
    
    while True:
        current_hand = theta_hand if current_player == 'Theta' else friend_hand
        current_slots = theta_slots if current_player == 'Theta' else friend_slots
        
        if not drawing_pile:
            break
        
        drawn_card = drawing_pile.pop(0)
        
        if drawn_card in current_hand:
            current_hand.remove(drawn_card)
            for i in range(2):
                if drawn_card == 'J' or drawn_card == str(i + 1):
                    if len(current_slots[i]) < 5:
                        current_slots[i].append(drawn_card)
                        if len(current_slots[0]) == 5 and len(current_slots[1]) == 5:
                            return current_player + ' wins'
                    else:
                        drawing_pile.append(drawn_card)
                        break
        else:
            drawing_pile.append(drawn_card)
            current_player = 'Theta' if current_player == 'Friend' else 'Friend'
    
    return 'Theta loses'

if __name__ == "__main__":
    shuffled_deck = input().strip()
    deck = initialize_deck()
    for card in shuffled_deck:
        deck.remove(card)
    print(play_game(deck)