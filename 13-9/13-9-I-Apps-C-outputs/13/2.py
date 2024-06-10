
import itertools

def get_hand(deck):
    # Get the first 10 cards for Theta
    hand = deck[:10]
    # Get the first 10 cards for the other player
    other_hand = deck[10:20]
    # Get the remaining cards in the deck
    deck = deck[20:]
    return hand, other_hand, deck

def get_slots(hand):
    # Get the number of cards in each slot
    slots = [0] * 10
    for card in hand:
        if card == 'A':
            slots[0] += 1
        elif card == '2':
            slots[1] += 1
        elif card == '3':
            slots[2] += 1
        elif card == '4':
            slots[3] += 1
        elif card == '5':
            slots[4] += 1
        elif card == '6':
            slots[5] += 1
        elif card == '7':
            slots[6] += 1
        elif card == '8':
            slots[7] += 1
        elif card == '9':
            slots[8] += 1
        elif card == 'T':
            slots[9] += 1
    return slots

def get_jack_slot(slots):
    # Get the index of the lowest-numbered slot with a Jack
    for i in range(10):
        if slots[i] == 1:
            return i
    return None

def get_next_card(deck):
    # Get the next card from the deck
    return deck[0]

def play_game(deck):
    # Get the hands and the deck
    hand, other_hand, deck = get_hand(deck)
    # Get the number of cards in each slot
    slots = get_slots(hand)
    # Get the index of the lowest-numbered slot with a Jack
    jack_slot = get_jack_slot(slots)
    # While there are cards in the deck
    while deck:
        # Get the next card from the deck
        card = get_next_card(deck)
        # If the card is a Jack
        if card == 'J':
            # If there is a slot with a Jack
            if jack_slot is not None:
                # Fill the Jack slot
                slots[jack_slot] -= 1
                # Get the next card from the deck
                card = get_next_card(deck)
        # If the card is a Queen or King
        if card in ['Q', 'K']:
            # Discard the card
            deck.pop(0)
        # If the card is a number
        if card in ['2', '3', '4', '5', '6', '7', '8', '9', 'T']:
            # Get the index of the slot for the card
            slot = int(card) - 1
            # If the slot has a card
            if slots[slot] > 0:
                # Fill the slot
                slots[slot] -= 1
            # Otherwise, discard the card
            else:
                deck.pop(0)
        # If the card is an Ace
        if card == 'A':
            # If there are slots with aces
            if any(slots[:5]):
                # Fill the lowest-numbered slot with an Ace
                slots[0] -= 1
            # Otherwise, discard the card
            else:
                deck.pop(0)
        # Check if Theta has won
        if not any(slots):
            return True
        # Check if the other player has won
        if not deck:
            return False
    return False

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input_ = f.readline().strip()
    deck = list(input_)
    result = play_game(deck)
    if result:
        print("Theta wins")
    else:
        print("Theta loses")

