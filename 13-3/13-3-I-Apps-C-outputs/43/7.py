
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
        # If the antique is not already in the dictionary, add it to the dictionary with its original cost
        if a[0] not in costs:
            costs[a[0]] = a[1]
        # If the antique is already in the dictionary and the current cost is less than the original cost, update the cost to the current cost
        elif a[1] < costs[a[0]]:
            costs[a[0]] = a[1]
        # If the current shop has not been visited before, add it to the set of visited shops
        if a[2] not in visited_shops:
            visited_shops.add(a[2])
        # Add the cost of the current antique to the total cost
        total_cost += a[1]
        # If the number of visited shops is equal to k, break out of the loop
        if len(visited_shops) == k:
            break
    # If the number of visited shops is less than k, return -1
    if len(visited_shops) < k:
        return -1
    # Return the total cost
    return total_cost

def main():
    n, m, k = map(int, input().split())
    antiques = []
    for i in range(n):
        antiques.append(list(map(int, input().split())))
    print(get_min_cost(n, m, k, antiques))

if __name__ == '__main__':
    main()

