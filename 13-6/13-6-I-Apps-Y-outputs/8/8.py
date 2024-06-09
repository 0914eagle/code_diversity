
import collections

def get_missing_cards(deck):
    # Initialize a dictionary to store the number of missing cards for each suit
    missing_cards = {"P": 0, "K": 0, "H": 0, "T": 0}
    
    # Initialize a dictionary to store the number of occurrences for each card
    card_counts = collections.defaultdict(int)
    
    # Loop through the deck and count the number of occurrences for each card
    for card in deck:
        card_counts[card] += 1
    
    # Loop through the deck and check if any card is missing or if there are two of the same card
    for card in deck:
        if card_counts[card] == 0:
            missing_cards[card[0]] += 1
        if card_counts[card] > 1:
            return "GRESKA"
    
    # Return the number of missing cards for each suit
    return missing_cards["P"], missing_cards["K"], missing_cards["H"], missing_cards["T"]

def main():
    deck = input()
    print(*get_missing_cards(deck))

if __name__ == '__main__':
    main()

