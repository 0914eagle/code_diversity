
def get_purchases(num_children, num_purchases, cards_per_child, children_purchases):
    # Initialize a dictionary to store the number of cards each child has
    cards = {i: cards_per_child for i in range(1, num_children + 1)}
    
    # Initialize a list to store the purchases
    purchases = []
    
    # Loop through each purchase
    for i in range(num_purchases):
        # Get the labels of the two children who made the purchase
        children = children_purchases[i]
        
        # Update the number of cards for each child
        cards[children[0]] -= 1
        cards[children[1]] -= 1
        
        # Add the purchase to the list of purchases
        purchases.append((children[0], children[1], cards[children[0]]))
    
    # Return the list of purchases
    return purchases

def get_winners(num_children, num_purchases, cards_per_child, children_purchases):
    # Get the list of purchases
    purchases = get_purchases(num_children, num_purchases, cards_per_child, children_purchases)
    
    # Initialize a dictionary to store the number of cards each child has
    cards = {i: cards_per_child for i in range(1, num_children + 1)}
    
    # Initialize a list to store the winners
    winners = []
    
    # Loop through each purchase
    for purchase in purchases:
        # Get the labels of the two children who made the purchase
        children = purchase[:2]
        
        # Update the number of cards for each child
        cards[children[0]] -= 1
        cards[children[1]] -= 1
        
        # Add the winner to the list of winners
        winners.append((children[0], children[1], cards[children[0]]))
    
    # Return the list of winners
    return winners

if __name__ == '__main__':
    num_children, num_purchases = map(int, input().split())
    cards_per_child = int(input())
    children_purchases = []
    for _ in range(num_purchases):
        children_purchases.append(tuple(map(int, input().split())))
    purchases = get_purchases(num_children, num_purchases, cards_per_child, children_purchases)
    winners = get_winners(num_children, num_purchases, cards_per_child, children_purchases)
    print(len(purchases))
    for purchase in purchases:
        print(*purchase)
    for winner in winners:
        print(*winner)

