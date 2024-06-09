
def get_danger(chemicals, reactions):
    # Initialize the danger as 1
    danger = 1
    # Loop through the reactions
    for x, y in reactions:
        # If the chemicals can react, multiply the danger by 2
        if x in chemicals and y in chemicals:
            danger *= 2
    # Return the danger
    return danger

def get_maximum_danger(n, m, reactions):
    # Initialize the maximum danger as 0
    maximum_danger = 0
    # Loop through all possible orders of pouring the chemicals
    for order in permutations(range(1, n + 1)):
        # Get the danger for the current order
        danger = get_danger(order, reactions)
        # If the danger is greater than the maximum danger, update the maximum danger
        if danger > maximum_danger:
            maximum_danger = danger
    # Return the maximum danger
    return maximum_danger

if __name__ == '__main__':
    n, m = map(int, input().split())
    reactions = [tuple(map(int, input().split())) for _ in range(m)]
    print(get_maximum_danger(n, m, reactions))

