
def get_input():
    n = int(input())
    edges = []
    for i in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    return n, edges

def is_reachable(n, edges, configuration):
    # Initialize a set to store the values that have been reached
    reached = set()
    
    # Add the initial value to the set
    reached.add(configuration[1])
    
    # Iterate through the edges of the tree
    for u, v in edges:
        # If the current value is not in the set, continue
        if configuration[u] not in reached:
            continue
        
        # If the other value is not in the set, add it
        if configuration[v] not in reached:
            reached.add(configuration[v])
    
    # Return True if all values have been reached, False otherwise
    return len(reached) == n

def solve(n, edges):
    # Initialize a dictionary to store the configuration of real numbers written on edges
    configuration = {}
    for i in range(1, n+1):
        configuration[i] = 0
    
    # Iterate through the edges of the tree
    for u, v in edges:
        # If the current value is not zero, continue
        if configuration[u] != 0 or configuration[v] != 0:
            continue
        
        # If the other value is zero, set it to one
        configuration[v] = 1
    
    # Return "YES" if all values have been reached, "NO" otherwise
    return "YES" if is_reachable(n, edges, configuration) else "NO"

def main():
    n, edges = get_input()
    print(solve(n, edges))

if __name__ == '__main__':
    main()

