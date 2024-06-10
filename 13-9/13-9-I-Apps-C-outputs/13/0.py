
import itertools

def get_deck(cards):
    
    deck = []
    for card in cards:
        if card in '23456789TJQKA':
            deck.append(card)
    return deck

def get_hands(deck, num_cards):
    
    hands = []
    for i in range(2):
        hands.append(deck[:num_cards])
        deck = deck[num_cards:]
    return hands

def get_slots(hand):
    
    slots = []
    for i in range(5):
        slots.append(hand[i])
    return slots

def get_cards_to_play(hand):
    
    cards_to_play = []
    for card in hand:
        if card not in 'JQKA':
            cards_to_play.append(card)
    return cards_to_play

def get_jacks(hand):
    
    jacks = []
    for card in hand:
        if card == 'J':
            jacks.append(card)
    return jacks

def get_next_card(deck):
    
    return deck[0]

def play_card(card, slots):
    
    updated_slots = []
    for i in range(5):
        if slots[i] == '':
            updated_slots.append(card)
            break
        else:
            updated_slots.append(slots[i])
    return updated_slots

def is_filled(slots):
    
    for slot in slots:
        if slot == '':
            return False
    return True

def is_valid_card(card, slots):
    
    if card == 'J':
        return True
    else:
        for i in range(5):
            if slots[i] == '':
                return True
            elif slots[i] == card:
                return False
    return False

def get_winner(hands):
    
    for hand in hands:
        if is_filled(get_slots(hand)):
            return hand
    return None

def play_game(deck):
    
    hands = get_hands(deck, 10)
    deck = deck[10:]
    while True:
        # Theta's turn
        slots = get_slots(hands[0])
        card = get_next_card(deck)
        if is_valid_card(card, slots):
            slots = play_card(card, slots)
            deck = deck[1:]
        else:
            deck = deck[1:]
        if is_filled(slots):
            break
        # Friend's turn
        slots = get_slots(hands[1])
        card = get_next_card(deck)
        if is_valid_card(card, slots):
            slots = play_card(card, slots)
            deck = deck[1:]
        else:
            deck = deck[1:]
        if is_filled(slots):
            break
    winner = get_winner(hands)
    if winner == hands[0]:
        return 'Theta wins'
    else:
        return 'Theta loses'

if __name__ == '__main__':
    cards = input()
    deck = get_deck(cards)
    print(play_game(deck))

