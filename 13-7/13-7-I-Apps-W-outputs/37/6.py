
def get_maximum_sum(a, edges):
    # Initialize a dictionary to store the pleasantness of each gift and the gifts that hang on it
    gifts = {}
    for i in range(len(a)):
        gifts[i + 1] = [a[i]]
    
    # Iterate through the edges and add the gifts that hang on each gift to the dictionary
    for edge in edges:
        u, v = edge[0], edge[1]
        if u in gifts:
            gifts[u].append(v)
        else:
            gifts[u] = [v]
    
    # Initialize a set to store the gifts that Chloe and Vladik have chosen
    chosen_gifts = set()
    
    # Function to recursively find the maximum sum of pleasantness of the gifts that Chloe and Vladik can choose
    def find_maximum_sum(gift, chosen_gifts):
        # If the gift has already been chosen, return 0
        if gift in chosen_gifts:
            return 0
        
        # If the gift has not been chosen, add it to the set of chosen gifts and find the maximum sum of pleasantness of the gifts that hang on it
        chosen_gifts.add(gift)
        maximum_sum = a[gift - 1]
        for hangs_on in gifts[gift]:
            maximum_sum += find_maximum_sum(hangs_on, chosen_gifts)
        
        return maximum_sum
    
    # Call the function with the first gift and an empty set of chosen gifts to find the maximum sum of pleasantness of the gifts that Chloe and Vladik can choose
    maximum_sum = find_maximum_sum(1, chosen_gifts)
    
    return maximum_sum

def main():
    n = int(input())
    a = list(map(int, input().split()))
    edges = []
    for i in range(n - 1):
        u, v = map(int, input().split())
        edges.append([u, v])
    
    maximum_sum = get_maximum_sum(a, edges)
    print(maximum_sum)

if __name__ == '__main__':
    main()

