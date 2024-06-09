
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
    
    # While there are still chemicals to pour
    while chemicals:
        # Find the chemical that can react with the least number of other chemicals
        min_reactions = len(chemicals)
        for x in chemicals:
            reactions_with_x = 0
            for y in chemicals:
                if x in chemicals and y in chemicals and x != y:
                    reactions_with_x += 1
            if reactions_with_x < min_reactions:
                min_reactions = reactions_with_x
                chosen_chemical = x
        
        # Add the chosen chemical to the order
        order.append(chosen_chemical)
        
        # Remove the chosen chemical and all its reactions from the chemicals and reactions
        chemicals.remove(chosen_chemical)
        reactions = [r for r in reactions if r[0] != chosen_chemical and r[1] != chosen_chemical]
    
    return order

def main():
    n, m = map(int, input().split())
    chemicals = set(range(1, n + 1))
    reactions = [tuple(map(int, input().split())) for _ in range(m)]
    order = get_optimal_order(chemicals, reactions)
    danger = get_danger(chemicals, reactions)
    print(danger)

if __name__ == '__main__':
    main()

