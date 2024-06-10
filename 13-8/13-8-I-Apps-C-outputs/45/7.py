
def purchase_cards(num_children, cards_per_child, purchase_pairs):
    # Initialize a dictionary to store the number of cards each child has
    cards = {i: 0 for i in range(1, num_children + 1)}
    
    # Initialize a list to store the purchases
    purchases = []
    
    # Loop through each purchase pair
    for pair in purchase_pairs:
        # Get the labels of the children who made the purchase
        child1, child2 = pair
        
        # Add the number of cards each child should get after the race
        cards[child1] += 1
        cards[child2] += 1
        
        # Add the purchase to the list of purchases
        purchases.append((child1, child2, 1))
    
    # Return the total number of purchases and the list of purchases
    return len(purchases), purchases

def solve_card_problem(num_children, cards_per_child, purchase_pairs, cards_won):
    # Call the purchase_cards function to get the total number of purchases and the list of purchases
    num_purchases, purchases = purchase_cards(num_children, cards_per_child, purchase_pairs)
    
    # Initialize a list to store the solutions
    solutions = []
    
    # Loop through each possible solution
    for solution in range(1, num_purchases + 1):
        # Check if the number of cards each child has after the purchases matches the given counts
        if all(cards_per_child[i] == cards[i] for i in range(1, num_children + 1)):
            # Add the solution to the list of solutions
            solutions.append(solution)
    
    # Return the list of solutions
    return solutions

def main():
    # Read the number of children and the number of purchases
    num_children, num_purchases = map(int, input().split())
    
    # Read the number of cards each child has
    cards_per_child = list(map(int, input().split()))
    
    # Read the pairs of children who made the purchases
    purchase_pairs = []
    for _ in range(num_purchases):
        purchase_pairs.append(tuple(map(int, input().split())))
    
    # Read the number of cards each child won in the races
    cards_won = list(map(int, input().split()))
    
    # Call the solve_card_problem function to get the list of solutions
    solutions = solve_card_problem(num_children, cards_per_child, purchase_pairs, cards_won)
    
    # Print the total number of purchases
    print(len(purchases))
    
    # Loop through each purchase
    for purchase in purchases:
        # Print the purchase
        print(*purchase)

if __name__ == '__main__':
    main()

