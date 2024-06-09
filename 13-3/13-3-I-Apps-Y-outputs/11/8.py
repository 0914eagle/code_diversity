
import collections

def solve(S):
    suits = ["P", "K", "H", "T"]
    cards = collections.defaultdict(int)
    for card in S.split():
        suit, num = card[0], int(card[1:])
        cards[suit] += 1
        if cards[suit] > 1:
            return "GRESKA"
    return " ".join(str(52 - cards[suit]) for suit in suits)

