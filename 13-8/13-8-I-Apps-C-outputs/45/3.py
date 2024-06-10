
def get_purchases(children_count, cards_count, purchases):
    # Initialize a dictionary to store the number of cards each child has
    cards = {i: 0 for i in range(1, children_count + 1)}
    
    # Initialize a list to store the purchases
    purchases_list = []
    
    # Loop through each purchase
    for purchase in purchases:
        # Get the labels of the children who made the purchase
        children = purchase.split()
        
        # Check if the children have enough cards to make the purchase
        if cards[int(children[0])] >= 2 and cards[int(children[1])] >= 2:
            # Subtract 2 cards from each child
            cards[int(children[0])] -= 2
            cards[int(children[1])] -= 2
            
            # Add the purchase to the list
            purchases_list.append([int(children[0]), int(children[1]), 2])
        elif cards[int(children[0])] >= 1 and cards[int(children[1])] >= 1:
            # Subtract 1 card from each child
            cards[int(children[0])] -= 1
            cards[int(children[1])] -= 1
            
            # Add the purchase to the list
            purchases_list.append([int(children[0]), int(children[1]), 1])
        else:
            # Add the purchase to the list with a 0 indicating that no cards were given
            purchases_list.append([int(children[0]), int(children[1]), 0])
    
    # Return the list of purchases
    return purchases_list

def get_winners(children_count, cards_count, purchases, winners):
    # Initialize a dictionary to store the number of cards each child has
    cards = {i: 0 for i in range(1, children_count + 1)}
    
    # Initialize a list to store the winners
    winners_list = []
    
    # Loop through each purchase
    for purchase in purchases:
        # Get the labels of the children who made the purchase
        children = purchase[0:2]
        
        # Check if the children have enough cards to make the purchase
        if cards[children[0]] >= 2 and cards[children[1]] >= 2:
            # Subtract 2 cards from each child
            cards[children[0]] -= 2
            cards[children[1]] -= 2
            
            # Add the winners to the list
            winners_list.append([children[0], children[1]])
        elif cards[children[0]] >= 1 and cards[children[1]] >= 1:
            # Subtract 1 card from each child
            cards[children[0]] -= 1
            cards[children[1]] -= 1
            
            # Add the winners to the list
            winners_list.append([children[0], children[1]])
        else:
            # Add the winners to the list with a 0 indicating that no cards were given
            winners_list.append([0, 0])
    
    # Return the list of winners
    return winners_list

if __name__ == '__main__':
    # Get the number of children and purchases
    children_count, purchases_count = map(int, input().split())
    
    # Get the initial cards count for each child
    cards_count = list(map(int, input().split()))
    
    # Get the purchases
    purchases = [input() for _ in range(purchases_count)]
    
    # Get the winners
    winners = get_winners(children_count, cards_count, purchases, [])
    
    # Print the total number of purchases
    print(len(purchases))
    
    # Print the purchases and winners
    for i in range(len(purchases)):
        print(purchases[i][0], purchases[i][1], winners[i][0])

