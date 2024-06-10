
def get_purchases(num_children, cards_per_child, purchases):
    # Initialize a dictionary to store the cards each child has
    cards = {i: 0 for i in range(1, num_children + 1)}
    
    # Initialize a list to store the purchases
    purchase_list = []
    
    # Loop through each purchase
    for purchase in purchases:
        # Get the two children involved in the purchase
        children = sorted(purchase)
        
        # Add the cards to the dictionary
        cards[children[0]] += 1
        cards[children[1]] += 1
        
        # Add the purchase to the list
        purchase_list.append(purchase)
    
    # Return the list of purchases
    return purchase_list

def get_winners(purchase_list, num_children):
    # Initialize a dictionary to store the winners of each race
    winners = {}
    
    # Loop through each purchase
    for purchase in purchase_list:
        # Get the two children involved in the purchase
        children = sorted(purchase)
        
        # If the two children have the same number of cards, they both win
        if cards[children[0]] == cards[children[1]]:
            winners[purchase] = [children[0], children[1]]
        # Otherwise, the child with the most cards wins
        else:
            winners[purchase] = [children[0] if cards[children[0]] > cards[children[1]] else children[1]]
    
    # Return the dictionary of winners
    return winners

def get_solution(num_children, cards_per_child, purchases):
    # Get the list of purchases
    purchase_list = get_purchases(num_children, cards_per_child, purchases)
    
    # Get the dictionary of winners
    winners = get_winners(purchase_list, num_children)
    
    # Initialize a list to store the solutions
    solution_list = []
    
    # Loop through each purchase
    for purchase in purchase_list:
        # Get the two children involved in the purchase
        children = sorted(purchase)
        
        # Get the number of cards the first child got after the race
        num_cards = 0 if winners[purchase][0] != children[0] else 1 if winners[purchase][0] != children[1] else 2
        
        # Add the solution to the list
        solution_list.append([children[0], children[1], num_cards])
    
    # Return the list of solutions
    return solution_list

if __name__ == '__main__':
    num_children, num_purchases = map(int, input().split())
    cards_per_child = list(map(int, input().split()))
    purchases = [list(map(int, input().split())) for _ in range(num_purchases)]
    solution = get_solution(num_children, cards_per_child, purchases)
    print(len(solution))
    for s in solution:
        print(*s)

