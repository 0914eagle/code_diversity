
def count_ways_to_swap(n, a, p):
    # Initialize a dictionary to store the number of apples on each node
    apples = {i: a[i-1] for i in range(1, n+1)}
    # Initialize a list to store the parents of each node
    parents = [p[i-1] for i in range(1, n+1)]
    # Initialize a set to store the nodes that have an even number of apples
    even_nodes = set()
    # Initialize a set to store the nodes that have an odd number of apples
    odd_nodes = set()
    
    # Loop through the nodes and update the sets of even and odd nodes
    for i in range(1, n+1):
        if apples[i] % 2 == 0:
            even_nodes.add(i)
        else:
            odd_nodes.add(i)
    
    # Initialize a variable to store the number of ways to swap nodes
    ways = 0
    
    # Loop through the nodes and check if swapping them will result in a win for Sagheer
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j and (i in even_nodes and j in odd_nodes or i in odd_nodes and j in even_nodes):
                ways += 1
    
    return ways

def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    print(count_ways_to_swap(n, a, p))

if __name__ == '__main__':
    main()

