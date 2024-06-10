
def get_purchases(num_children, num_purchases, cards_per_child, purchase_list):
    # Initialize a dictionary to store the number of cards each child has
    cards_dict = {i: cards_per_child for i in range(1, num_children + 1)}
    
    # Initialize a list to store the purchases
    purchases = []
    
    # Loop through each purchase
    for i in range(num_purchases):
        # Get the two children who made the purchase
        children = purchase_list[i]
        
        # Get the number of cards each child got
        num_cards = 2
        
        # Update the number of cards each child has
        cards_dict[children[0]] += num_cards
        cards_dict[children[1]] += num_cards
        
        # Add the purchase to the list of purchases
        purchases.append((children[0], children[1], num_cards))
    
    return purchases

def get_winners(purchases, cards_per_child):
    # Initialize a dictionary to store the number of cards each child has
    cards_dict = {i: cards_per_child for i in range(1, len(purchases) + 1)}
    
    # Initialize a list to store the winners
    winners = []
    
    # Loop through each purchase
    for i in range(len(purchases)):
        # Get the two children who made the purchase
        children = purchases[i]
        
        # Get the number of cards each child got
        num_cards = children[2]
        
        # Update the number of cards each child has
        cards_dict[children[0]] += num_cards
        cards_dict[children[1]] += num_cards
        
        # Add the winner to the list of winners
        winners.append(children[0])
    
    return winners

def main():
    # Get the input
    num_children, num_purchases = map(int, input().split())
    cards_per_child = int(input())
    purchase_list = []
    for i in range(num_purchases):
        purchase_list.append(tuple(map(int, input().split())))
    
    # Get the purchases
    purchases = get_purchases(num_children, num_purchases, cards_per_child, purchase_list)
    
    # Get the winners
    winners = get_winners(purchases, cards_per_child)
    
    # Print the output
    print(len(purchases))
    for purchase in purchases:
        print(purchase[0], purchase[1], purchase[2])
    
    for winner in winners:
        print(winner)

if __name__ == '__main__':
    main()

