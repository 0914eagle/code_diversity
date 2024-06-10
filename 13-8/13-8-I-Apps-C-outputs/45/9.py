
def get_purchases(num_children, current_cards, purchases):
    # Initialize a dictionary to store the number of cards each child has
    cards = {i: current_cards[i-1] for i in range(1, num_children+1)}
    
    # Initialize a list to store the purchases
    purchases_list = []
    
    # Iterate over the purchases
    for purchase in purchases:
        # Get the two children who made the purchase
        children = purchase[0], purchase[1]
        
        # Get the number of cards each child has
        cards1 = cards[children[0]]
        cards2 = cards[children[1]]
        
        # Determine who won the race
        if cards1 > cards2:
            winner = children[0]
        elif cards1 < cards2:
            winner = children[1]
        else:
            winner = None
        
        # Update the number of cards each child has
        if winner == children[0]:
            cards[children[0]] += 2
            cards[children[1]] += 1
        elif winner == children[1]:
            cards[children[1]] += 2
            cards[children[0]] += 1
        else:
            cards[children[0]] += 1
            cards[children[1]] += 1
        
        # Add the purchase to the list
        purchases_list.append((children[0], children[1], winner))
    
    return purchases_list

def get_solution(num_children, current_cards, purchases):
    # Get the purchases
    purchases_list = get_purchases(num_children, current_cards, purchases)
    
    # Initialize a list to store the solution
    solution = []
    
    # Iterate over the purchases
    for purchase in purchases_list:
        # Get the two children who made the purchase
        children = purchase[0], purchase[1]
        
        # Get the number of cards each child has
        cards1 = cards[children[0]]
        cards2 = cards[children[1]]
        
        # Determine who won the race
        if cards1 > cards2:
            winner = children[0]
        elif cards1 < cards2:
            winner = children[1]
        else:
            winner = None
        
        # Add the solution to the list
        solution.append((children[0], children[1], winner))
    
    return solution

if __name__ == '__main__':
    num_children, num_purchases = map(int, input().split())
    current_cards = list(map(int, input().split()))
    purchases = []
    for _ in range(num_purchases):
        purchases.append(list(map(int, input().split())))
    solution = get_solution(num_children, current_cards, purchases)
    print(len(solution))
    for purchase in solution:
        print(*purchase)

