
def get_cycle_length(n, a):
    # Initialize a dictionary to store the nodes and their neighbors
    neighbors = {}
    for i in range(n):
        neighbors[i] = []
    
    # Populate the dictionary with the nodes and their neighbors
    for i in range(n):
        for j in range(i+1, n):
            if a[i] & a[j] != 0:
                neighbors[i].append(j)
                neighbors[j].append(i)
    
    # Use Breadth-First Search to find the shortest cycle
    queue = []
    visited = set()
    for i in range(n):
        if i not in visited:
            queue.append(i)
            visited.add(i)
            while queue:
                node = queue.pop(0)
                for neighbor in neighbors[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                        if neighbor == i:
                            return len(visited)
    
    # If no cycle is found, return -1
    return -1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_cycle_length(n, a))

if __name__ == '__main__':
    main()

