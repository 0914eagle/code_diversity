
def get_danger(chemicals, reactions):
    # Initialize the danger as 1
    danger = 1
    
    # Iterate over the reactions
    for reaction in reactions:
        # Get the indices of the chemicals involved in the reaction
        x, y = reaction
        
        # If the chemicals are already in the test tube, multiply the danger by 2
        if x in chemicals and y in chemicals:
            danger *= 2
    
    return danger

def get_optimal_order(chemicals, reactions):
    # Initialize the optimal order as an empty list
    optimal_order = []
    
    # Iterate over the chemicals
    for chemical in chemicals:
        # If the chemical is not already in the test tube, add it to the optimal order
        if chemical not in optimal_order:
            optimal_order.append(chemical)
    
    return optimal_order

def get_maximum_danger(chemicals, reactions):
    # Get the optimal order
    optimal_order = get_optimal_order(chemicals, reactions)
    
    # Get the danger for the optimal order
    danger = get_danger(optimal_order, reactions)
    
    return danger

if __name__ == '__main__':
    n, m = map(int, input().split())
    chemicals = list(range(1, n + 1))
    reactions = []
    for _ in range(m):
        x, y = map(int, input().split())
        reactions.append((x, y))
    print(get_maximum_danger(chemicals, reactions))

