
def get_best_cards(golds, silvers, coppers):
    # Initialize variables
    victory_points = 0
    buying_power = golds * 3 + silvers * 2 + coppers
    best_victory_card = ""
    best_treasure_card = ""

    # Iterate through the victory cards
    for card in ["Province", "Duchy", "Estate"]:
        card_cost = 0
        if card == "Province":
            card_cost = 8
        elif card == "Duchy":
            card_cost = 5
        elif card == "Estate":
            card_cost = 2

        # Check if the card is within buying power
        if card_cost <= buying_power:
            # Calculate the victory points
            victory_points += get_victory_points(card)
            # Update the best victory card
            best_victory_card = card
            # Update the buying power
            buying_power -= card_cost

    # Iterate through the treasure cards
    for card in ["Gold", "Silver", "Copper"]:
        card_cost = 0
        if card == "Gold":
            card_cost = 6
        elif card == "Silver":
            card_cost = 3
        elif card == "Copper":
            card_cost = 0

        # Check if the card is within buying power
        if card_cost <= buying_power:
            # Calculate the buying power
            buying_power += get_buying_power(card)
            # Update the best treasure card
            best_treasure_card = card

    # Return the best victory card and treasure card
    return f"{best_victory_card} or {best_treasure_card}"

def get_victory_points(card):
    if card == "Province":
        return 6
    elif card == "Duchy":
        return 3
    elif card == "Estate":
        return 1
    else:
        return 0

def get_buying_power(card):
    if card == "Gold":
        return 3
    elif card == "Silver":
        return 2
    elif card == "Copper":
        return 1
    else:
        return 0

if __name__ == '__main__':
    golds, silvers, coppers = map(int, input().split())
    print(get_best_cards(golds, silvers, coppers))

