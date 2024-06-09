
import re

def solve(s):
    # Initialize a dictionary to store the count of each suit
    suit_count = {"P": 0, "K": 0, "H": 0, "T": 0}
    
    # Initialize a set to store the labels of the cards
    card_labels = set()
    
    # Iterate through the string and extract the labels of the cards
    for label in re.findall(r"[A-Z0-9]{3}", s):
        card_labels.add(label)
    
    # Iterate through the labels of the cards and increment the count of each suit
    for label in card_labels:
        suit = label[0]
        suit_count[suit] += 1
    
    # Check if there are two exact same cards in the deck
    if len(card_labels) != 52:
        return "GRESKA"
    
    # Return the count of each suit
    return " ".join(str(suit_count[suit]) for suit in ["P", "K", "H", "T"])

