
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
    # Loop through each antique again
    for a in antiques:
        # If the antique is already in the dictionary and the current cost is greater than the original cost, remove it from the dictionary
        if a[1] > costs[a[0]]:
            del costs[a[0]]
    # If the dictionary is empty, it is not possible to collect all of the antiques while visiting no more than k stores, so return -1
    if not costs:
        return -1
    # Otherwise, return the sum of the costs of the antiques in the dictionary
    return sum(costs.values())

def main():
    n, m, k = map(int, input().split())
    antiques = []
    for i in range(n):
        a, p, b, q = map(int, input().split())
        antiques.append([a, p, b, q])
    print(get_min_cost(n, m, k, antiques))

if __name__ == '__main__':
    main()

