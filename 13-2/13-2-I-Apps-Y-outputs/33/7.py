
def get_best_cards(golds, silvers, coppers):
    # Initialize the best victory card and best treasure card
    best_victory_card = ""
    best_treasure_card = ""
    
    # Calculate the total buying power
    total_buying_power = golds * 3 + silvers * 2 + coppers
    
    # Iterate over the victory cards and find the best one that Jake can buy
    for victory_card in ["Province", "Duchy", "Estate"]:
        if victory_card == "Province":
            victory_card_cost = 8
            victory_card_value = 6
        elif victory_card == "Duchy":
            victory_card_cost = 5
            victory_card_value = 3
        else:
            victory_card_cost = 2
            victory_card_value = 1
            
        if victory_card_cost <= total_buying_power:
            best_victory_card = victory_card
            break
    
    # Iterate over the treasure cards and find the best one that Jake can buy
    for treasure_card in ["Gold", "Silver", "Copper"]:
        if treasure_card == "Gold":
            treasure_card_cost = 6
            treasure_card_value = 3
        elif treasure_card == "Silver":
            treasure_card_cost = 3
            treasure_card_value = 2
        else:
            treasure_card_cost = 0
            treasure_card_value = 1
            
        if treasure_card_cost <= total_buying_power:
            best_treasure_card = treasure_card
            break
    
    # Return the best victory card and best treasure card
    if best_victory_card != "":
        return best_victory_card + " or " + best_treasure_card
    else:
        return best_treasure_card

if __name__ == '__main__':
    golds = int(input())
    silvers = int(input())
    coppers = int(input())
    print(get_best_cards(golds, silvers, coppers))

