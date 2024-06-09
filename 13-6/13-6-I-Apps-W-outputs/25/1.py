
def get_danger(chemicals, reactions):
    # Initialize the danger as 1
    danger = 1
    
    # Iterate over the reactions
    for x, y in reactions:
        # If the chemicals can react, multiply the danger by 2
        if x in chemicals and y in chemicals:
            danger *= 2
    
    return danger

def get_optimal_order(chemicals, reactions):
    # Initialize the optimal order as an empty list
    order = []
    
    # While there are still chemicals that haven't been added to the order
    while len(order) < len(chemicals):
        # Find the chemical that can react with the most other chemicals
        max_reactants = 0
        for x in chemicals:
            reactants = 0
            for y in chemicals:
                if x in chemicals and y in chemicals and (x, y) in reactions:
                    reactants += 1
            if reactants > max_reactants:
                max_reactants = reactants
                optimal_chemical = x
        
        # Add the optimal chemical to the order
        order.append(optimal_chemical)
        chemicals.remove(optimal_chemical)
    
    return order

def main():
    n, m = map(int, input().split())
    chemicals = set(range(1, n + 1))
    reactions = []
    for _ in range(m):
        x, y = map(int, input().split())
        reactions.append((x, y))
    
    order = get_optimal_order(chemicals, reactions)
    danger = get_danger(chemicals, reactions)
    print(danger)

if __name__ == '__main__':
    main()

