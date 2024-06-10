
def get_purchases(num_children, num_purchases, cards_per_child, purchases):
    # Initialize a dictionary to store the cards each child has
    cards = {i: 0 for i in range(1, num_children + 1)}
    
    # Initialize a list to store the purchases
    purchase_list = []
    
    # Loop through each purchase
    for i in range(num_purchases):
        # Get the two children who made the purchase
        children = purchases[i]
        
        # Add the cards to the dictionary
        cards[children[0]] += 1
        cards[children[1]] += 1
        
        # Add the purchase to the list
        purchase_list.append([children[0], children[1], 0])
    
    # Loop through each child
    for i in range(num_children):
        # If the child has an odd number of cards
        if cards[i] % 2 == 1:
            # Find the child who has the same number of cards
            for j in range(i + 1, num_children):
                if cards[j] == cards[i]:
                    # Add the purchase to the list
                    purchase_list.append([i, j, 1])
                    break
    
    return purchase_list

def get_winners(purchase_list):
    # Initialize a dictionary to store the winners of each purchase
    winners = {}
    
    # Loop through each purchase
    for i in range(len(purchase_list)):
        # Get the two children who made the purchase
        children = purchase_list[i][:2]
        
        # If the first child won the race
        if purchase_list[i][2] == 0:
            # Add the first child to the winners dictionary
            winners[i] = children[0]
        # If the second child won the race
        elif purchase_list[i][2] == 1:
            # Add the second child to the winners dictionary
            winners[i] = children[1]
    
    return winners

def main():
    # Get the number of children and purchases
    num_children, num_purchases = map(int, input().split())
    
    # Get the number of cards each child has
    cards_per_child = list(map(int, input().split()))
    
    # Get the purchases
    purchases = []
    for i in range(num_purchases):
        purchases.append(list(map(int, input().split())))
    
    # Get the list of purchases
    purchase_list = get_purchases(num_children, num_purchases, cards_per_child, purchases)
    
    # Get the winners of each purchase
    winners = get_winners(purchase_list)
    
    # Print the number of purchases
    print(len(purchase_list))
    
    # Loop through each purchase
    for i in range(len(purchase_list)):
        # Print the purchase
        print(*purchase_list[i], winners[i])

if __name__ == '__main__':
    main()

