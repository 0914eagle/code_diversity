
def read_input():
    n, k = map(int, input().split())
    return n, k

def write_plaques(n, k):
    # Initialize a list to store the plaques
    plaques = [0] * (n + 1)
    
    # Initialize a set to store the visited houses
    visited = set()
    
    # Initialize a counter to keep track of the number of ways to write the plaques
    count = 0
    
    # Start by writing the plaques for the first k houses
    for i in range(1, k + 1):
        plaques[i] = i
        visited.add(i)
    
    # While there are still unvisited houses
    while len(visited) < n:
        # Find the next unvisited house
        for i in range(1, n + 1):
            if i not in visited:
                break
        
        # Find the next plaque number that has not been used
        for j in range(1, n + 1):
            if j not in visited and j not in plaques:
                break
        
        # Write the plaque number on the unvisited house
        plaques[i] = j
        visited.add(i)
        visited.add(j)
        
        # If the unvisited house is k + 1 or more, we can return to house number 1
        if i >= k + 1:
            count += 1
    
    # Return the number of ways to write the plaques
    return count

def main():
    n, k = read_input()
    print(write_plaques(n, k) % 1000000007)

if __name__ == '__main__':
    main()

