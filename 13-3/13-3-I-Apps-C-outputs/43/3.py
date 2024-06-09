
def get_min_cost(n, m, k, antiques):
    # Initialize a dictionary to store the cost of each antique
    costs = {}
    # Iterate over the antiques
    for a in antiques:
        # Get the original and knock-off prices of the current antique
        original_price, knockoff_price = a[1], a[3]
        # If the current antique is not in the dictionary, add it to the dictionary with its original price
        if a[0] not in costs:
            costs[a[0]] = original_price
        # If the current antique is already in the dictionary and the knock-off price is lower, update the price to the knock-off price
        elif knockoff_price < costs[a[0]]:
            costs[a[0]] = knockoff_price
    # Sort the dictionary by value (price) in ascending order
    sorted_costs = sorted(costs.items(), key=lambda x: x[1])
    # Initialize a variable to store the total cost
    total_cost = 0
    # Iterate over the sorted dictionary
    for i in range(k):
        # Add the current price to the total cost
        total_cost += sorted_costs[i][1]
    # Return the total cost
    return total_cost

def main():
    # Read the input data
    n, m, k = map(int, input().split())
    antiques = []
    for i in range(n):
        antiques.append(list(map(int, input().split())))
    # Call the get_min_cost function and print the result
    print(get_min_cost(n, m, k, antiques))

if __name__ == '__main__':
    main()

