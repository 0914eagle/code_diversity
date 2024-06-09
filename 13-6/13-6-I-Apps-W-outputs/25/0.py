
def get_danger_order(chemicals, reactions):
    # Initialize the danger array with 1 for each chemical
    danger = [1] * len(chemicals)

    # Iterate over the reactions and update the danger array
    for x, y in reactions:
        danger[x - 1] *= 2
        danger[y - 1] *= 2

    # Return the maximum danger
    return max(danger)

def get_optimal_order(chemicals, reactions):
    # Initialize the optimal order with the first chemical
    order = [chemicals[0]]

    # Iterate over the remaining chemicals
    for i in range(1, len(chemicals)):
        # Find the chemical that will result in the maximum danger when added to the current order
        max_danger = 0
        for j in range(len(order)):
            if get_danger_order(order[:j] + [chemicals[i]] + order[j:], reactions) > max_danger:
                max_danger = get_danger_order(order[:j] + [chemicals[i]] + order[j:], reactions)
                optimal_position = j

        # Add the chemical to the optimal position in the order
        order.insert(optimal_position, chemicals[i])

    # Return the optimal order
    return order

if __name__ == '__main__':
    chemicals, reactions = map(int, input().split())
    chemicals = list(range(1, chemicals + 1))
    reactions = [tuple(map(int, input().split())) for _ in range(reactions)]
    print(get_optimal_order(chemicals, reactions))

