
def get_missing_cards(deck):
    suits = ["P", "K", "H", "T"]
    numbers = [str(i) for i in range(1, 14)]
    missing_cards = [0, 0, 0, 0]
    
    for card in deck:
        suit = card[0]
        number = card[1:]
        if suit in suits and number in numbers:
            suits.remove(suit)
            numbers.remove(number)
        else:
            return "GRESKA"
    
    for i in range(len(suits)):
        missing_cards[i] = len(suits) - i
    
    return " ".join(str(card) for card in missing_cards)

def main():
    deck = input()
    print(get_missing_cards(deck))

if __name__ == '__main__':
    main()

