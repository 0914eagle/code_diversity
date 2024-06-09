
def get_min_cost(n, m, k, antiques):
    # Initialize a dictionary to store the cost of each antique
    costs = {}
    # Loop through each antique
    for a in antiques:
        # If the antique is not already in the dictionary, add it to the dictionary with its original cost
        if a[0] not in costs:
            costs[a[0]] = a[1]
        # If the antique is already in the dictionary and the current cost is less than the original cost, update the cost to the current cost
        elif a[1] < costs[a[0]]:
            costs[a[0]] = a[1]
    # Initialize a set to store the visited shops
    visited_shops = set()
    # Initialize a variable to store the total cost
    total_cost = 0
    # Loop through each antique
    for a in antiques:
        # If the shop that sells the antique is not in the visited shops set, add it to the visited shops set and add the cost of the antique to the total cost
        if a[0] not in visited_shops:
            visited_shops.add(a[0])
            total_cost += costs[a[0]]
        # If the shop that sells the antique is already in the visited shops set, add the cost of the knock-off version of the antique to the total cost
        else:
            total_cost += a[3]
    # If the total cost is less than or equal to the minimum cost, return the total cost
    if total_cost <= k * 1000000:
        return total_cost
    # If the total cost is greater than the minimum cost, return -1
    else:
        return -1

def main():
    n, m, k = map(int, input().split())
    antiques = []
    for i in range(n):
        a, p, b, q = map(int, input().split())
        antiques.append([a, p, b, q])
    print(get_min_cost(n, m, k, antiques))

if __name__ == '__main__':
    main()

