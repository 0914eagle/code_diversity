
import re

def solve(S):
    # Initialize a dictionary to store the count of each suit
    suit_count = {"P": 0, "K": 0, "H": 0, "T": 0}
    
    # Initialize a set to store the labels of the cards
    card_labels = set()
    
    # Iterate through the string S and extract the labels of the cards
    for label in re.findall(r"[A-Z][0-9]{2}", S):
        card_labels.add(label)
    
    # Iterate through the dictionary of suits and increment the count for each suit
    for suit in suit_count:
        for label in card_labels:
            if suit in label:
                suit_count[suit] += 1
    
    # Check if there are two exact same cards in the deck
    if len(card_labels) != 52:
        return "GRESKA"
    
    # Return the count of each suit
    return " ".join(str(suit_count[suit]) for suit in suit_count)

