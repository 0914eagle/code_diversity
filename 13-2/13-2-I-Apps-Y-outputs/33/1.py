
def get_best_card(golds, silvers, coppers):
    # Initialize the best card variables
    best_victory_card = ""
    best_treasure_card = ""
    
    # Calculate the total buying power
    total_buying_power = golds * 3 + silvers * 2 + coppers
    
    # Iterate over the victory cards
    for card in ["Province", "Duchy", "Estate"]:
        # Get the cost of the current card
        cost = 0
        if card == "Province":
            cost = 8
        elif card == "Duchy":
            cost = 5
        elif card == "Estate":
            cost = 2
            
        # Check if the card is within budget
        if cost <= total_buying_power:
            # Update the best victory card
            best_victory_card = card
            break
    
    # Iterate over the treasure cards
    for card in ["Gold", "Silver", "Copper"]:
        # Get the cost of the current card
        cost = 0
        if card == "Gold":
            cost = 6
        elif card == "Silver":
            cost = 3
        elif card == "Copper":
            cost = 0
            
        # Check if the card is within budget
        if cost <= total_buying_power:
            # Update the best treasure card
            best_treasure_card = card
            break
    
    # Return the best card
    if best_victory_card != "":
        return best_victory_card + " or " + best_treasure_card
    else:
        return best_treasure_card

if __name__ == '__main__':
    golds = int(input())
    silvers = int(input())
    coppers = int(input())
    print(get_best_card(golds, silvers, coppers))

