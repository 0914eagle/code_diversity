
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
    while chemicals:
        # Find the chemical that can be added to the order without causing a reaction
        for chemical in chemicals:
            if not any(x == chemical or y == chemical for x, y in reactions):
                break
        # Add the chemical to the order
        order.append(chemical)
        # Remove the chemical from the list of chemicals
        chemicals.remove(chemical)
    return order

def get_maximum_danger(chemicals, reactions):
    # Get the optimal order
    order = get_optimal_order(chemicals, reactions)
    # Get the danger for the optimal order
    danger = get_danger(chemicals, reactions)
    return danger

if __name__ == '__main__':
    n, m = map(int, input().split())
    chemicals = list(range(1, n + 1))
    reactions = [tuple(map(int, input().split())) for _ in range(m)]
    print(get_maximum_danger(chemicals, reactions))

