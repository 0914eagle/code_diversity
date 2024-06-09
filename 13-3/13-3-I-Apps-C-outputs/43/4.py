
def get_min_cost(n, m, k, antiques):
    # Initialize a dictionary to store the cost of each antique
    costs = {}
    # Loop through each antique
    for a in antiques:
        # Get the original and knock-off prices of the antique
        original_price, knockoff_price = a[1], a[3]
        # If the original price is less than the knock-off price, swap them
        if original_price > knockoff_price:
            original_price, knockoff_price = knockoff_price, original_price
        # Add the cost of the antique to the dictionary
        costs[a[0]] = original_price
    # Initialize a set to store the visited shops
    visited_shops = set()
    # Initialize a variable to store the total cost
    total_cost = 0
    # Loop through each antique
    for i in range(n):
        # Get the index of the shop that sells the original version of the antique
        shop_index = antiques[i][0]
        # If the shop has not been visited yet, visit it and add the cost of the antique to the total cost
        if shop_index not in visited_shops:
            visited_shops.add(shop_index)
            total_cost += costs[i]
        # If the shop has been visited, add the cost of the knock-off version of the antique to the total cost
        else:
            total_cost += costs[i]
    # If the total cost is less than or equal to the maximum cost, return the total cost
    if total_cost <= k:
        return total_cost
    # Otherwise, return -1
    else:
        return -1

def main():
    n, m, k = map(int, input().split())
    antiques = []
    for i in range(n):
        antiques.append(list(map(int, input().split())))
    print(get_min_cost(n, m, k, antiques))

if __name__ == '__main__':
    main()

