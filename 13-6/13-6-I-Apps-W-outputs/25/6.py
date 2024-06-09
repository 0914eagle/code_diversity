
def get_danger_level(chemicals, reactions):
    # Initialize the danger level to 1
    danger_level = 1
    
    # Iterate over the reactions
    for x, y in reactions:
        # If the current chemical can react with the previous chemical
        if x in chemicals and y in chemicals:
            # Multiply the danger level by 2
            danger_level *= 2
    
    # Return the danger level
    return danger_level

def get_optimal_order(chemicals, reactions):
    # Initialize the optimal order as an empty list
    optimal_order = []
    
    # While there are still chemicals to pour
    while chemicals:
        # Find the chemical that can react with the most number of other chemicals
        most_reactions = 0
        for x in chemicals:
            # Count the number of reactions with other chemicals
            num_reactions = 0
            for y in chemicals:
                if x in chemicals and y in chemicals and (x, y) in reactions:
                    num_reactions += 1
            # If the current chemical can react with more chemicals than the previous one
            if num_reactions > most_reactions:
                # Set the current chemical as the most reactive
                most_reactions = num_reactions
                most_reactive = x
        # Add the most reactive chemical to the optimal order
        optimal_order.append(most_reactive)
        # Remove the most reactive chemical from the list of chemicals
        chemicals.remove(most_reactive)
    
    # Return the optimal order
    return optimal_order

def get_maximum_danger(chemicals, reactions):
    # Get the optimal order of pouring the chemicals
    optimal_order = get_optimal_order(chemicals, reactions)
    # Get the danger level of the optimal order
    danger_level = get_danger_level(chemicals, reactions)
    # Return the maximum danger level
    return danger_level

if __name__ == '__main__':
    n, m = map(int, input().split())
    chemicals = set(range(1, n + 1))
    reactions = []
    for _ in range(m):
        x, y = map(int, input().split())
        reactions.append((x, y))
    print(get_maximum_danger(chemicals, reactions))

