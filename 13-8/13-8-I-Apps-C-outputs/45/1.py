
def get_purchases(num_children, num_purchases, current_cards, purchase_pairs):
    # Initialize a dictionary to keep track of the cards each child has
    cards = {i: current_cards[i-1] for i in range(1, num_children+1)}
    # Initialize a list to store the purchases
    purchases = []
    
    # Loop through each purchase pair
    for i in range(num_purchases):
        # Get the labels of the two children who made the purchase
        a, b = purchase_pairs[i]
        # Calculate the number of cards each child got after the race
        cards_a = cards[a] // 2
        cards_b = cards[b] // 2
        # Update the number of cards each child has
        cards[a] -= cards_a
        cards[b] -= cards_b
        # Add the purchase to the list of purchases
        purchases.append([a, b, cards_a])
    
    return purchases

def get_winners(purchases):
    # Initialize a dictionary to keep track of the winners for each purchase
    winners = {}
    
    # Loop through each purchase
    for i, purchase in enumerate(purchases):
        # Get the labels of the two children who made the purchase
        a, b = purchase[0:2]
        # Get the number of cards each child got after the race
        cards_a = purchase[2]
        cards_b = purchase[3]
        # Check if one child got all the cards
        if cards_a == 0:
            winners[i] = a
        elif cards_b == 0:
            winners[i] = b
    
    return winners

def get_solution(num_children, current_cards, purchase_pairs):
    # Get the purchases made by the children
    purchases = get_purchases(num_children, len(purchase_pairs), current_cards, purchase_pairs)
    # Get the winners of each purchase
    winners = get_winners(purchases)
    # Return the solution
    return winners

if __name__ == '__main__':
    num_children, num_purchases = map(int, input().split())
    current_cards = list(map(int, input().split()))
    purchase_pairs = []
    for _ in range(num_purchases):
        a, b = map(int, input().split())
        purchase_pairs.append([a, b])
    solution = get_solution(num_children, current_cards, purchase_pairs)
    print(len(solution))
    for i, winner in solution.items():
        print(winner, end=' ')

