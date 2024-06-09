
def get_best_cards(golds, silvers, coppers):
    # Initialize the best victory card and best treasure card
    best_victory_card = ""
    best_treasure_card = ""
    
    # Calculate the total buying power
    total_buying_power = golds * 3 + silvers * 2 + coppers
    
    # Iterate over the victory cards and find the best one
    for victory_card in ["Province", "Duchy", "Estate"]:
        # Get the cost of the victory card
        cost = 0
        if victory_card == "Province":
            cost = 8
        elif victory_card == "Duchy":
            cost = 5
        elif victory_card == "Estate":
            cost = 2
        
        # Check if the victory card is within budget
        if cost <= total_buying_power:
            # Update the best victory card
            best_victory_card = victory_card
            break
    
    # Iterate over the treasure cards and find the best one
    for treasure_card in ["Gold", "Silver", "Copper"]:
        # Get the cost of the treasure card
        cost = 0
        if treasure_card == "Gold":
            cost = 6
        elif treasure_card == "Silver":
            cost = 3
        elif treasure_card == "Copper":
            cost = 0
        
        # Check if the treasure card is within budget
        if cost <= total_buying_power:
            # Update the best treasure card
            best_treasure_card = treasure_card
            break
    
    # Return the best victory card and treasure card
    if best_victory_card != "":
        return best_victory_card + " or " + best_treasure_card
    else:
        return best_treasure_card

if __name__ == '__main__':
    golds = int(input())
    silvers = int(input())
    coppers = int(input())
    print(get_best_cards(golds, silvers, coppers))

