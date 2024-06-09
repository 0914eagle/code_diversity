
def get_best_card(golds, silvers, coppers):
    # Initialize variables
    victory_points = 0
    treasure_cards = []

    # Calculate victory points and treasure cards
    if golds >= 2:
        victory_points += 3
        treasure_cards.append("Gold")
    if silvers >= 2:
        victory_points += 2
        treasure_cards.append("Silver")
    if coppers >= 1:
        victory_points += 1
        treasure_cards.append("Copper")

    # Determine the best card to buy
    if victory_points >= 6:
        return "Province"
    elif victory_points >= 3:
        return "Duchy"
    elif victory_points >= 1:
        return "Estate"
    else:
        return treasure_cards[0]

def main():
    golds, silvers, coppers = map(int, input().split())
    print(get_best_card(golds, silvers, coppers))

if __name__ == '__main__':
    main()

