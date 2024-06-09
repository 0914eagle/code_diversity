
def solve_problem(n, m, c_l, c_e, v, queries):
    # Initialize a dictionary to store the shortest distance from each section to the elevator or stairs
    dist = {}
    for i in range(1, n+1):
        for j in range(1, m+1):
            dist[(i, j)] = float('inf')
    
    # Initialize a queue to perform BFS
    queue = []
    
    # Enqueue the starting section (1, 1) with distance 0
    queue.append(((1, 1), 0))
    
    # Loop until the queue is empty
    while queue:
        # Dequeue the current section and its distance
        current_section, current_dist = queue.pop(0)
        
        # If the current section is the destination, return the distance
        if current_section == (n, m):
            return current_dist
        
        # Get the floor and section number of the current section
        current_floor, current_section_num = current_section
        
        # If the current section is not occupied by stairs or elevators, enqueue its neighbors with the updated distance
        if current_section_num not in l and current_section_num not in e:
            for neighbor in get_neighbors(current_section, n, m):
                queue.append((neighbor, current_dist+1))
        
        # If the current section is occupied by stairs, enqueue the sections above it with the updated distance
        if current_section_num in l:
            for i in range(current_floor+1, n+1):
                queue.append(((i, current_section_num), current_dist+1))
        
        # If the current section is occupied by elevators, enqueue the sections above it with the updated distance
        if current_section_num in e:
            for i in range(current_floor+1, n+1):
                queue.append(((i, current_section_num), current_dist+v))
    
    # If the destination is not reachable, return -1
    return -1

def get_neighbors(section, n, m):
    # Get the floor and section number of the current section
    current_floor, current_section_num = section
    
    # Initialize a list to store the neighbors
    neighbors = []
    
    # If the current section is not on the last floor, enqueue the section below it
    if current_floor < n:
        neighbors.append((current_floor+1, current_section_num))
    
    # If the current section is not on the first floor, enqueue the section above it
    if current_floor > 1:
        neighbors.append((current_floor-1, current_section_num))
    
    # If the current section is not on the first section, enqueue the section to the left of it
    if current_section_num > 1:
        neighbors.append((current_floor, current_section_num-1))
    
    # If the current section is not on the last section, enqueue the section to the right of it
    if current_section_num < m:
        neighbors.append((current_floor, current_section_num+1))
    
    return neighbors

def main():
    n, m, c_l, c_e, v = map(int, input().split())
    l = set(map(int, input().split()))
    e = set(map(int, input().split()))
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(tuple(map(int, input().split())))
    
    for query in queries:
        print(solve_problem(n, m, c_l, c_e, v, query))

if __name__ == '__main__':
    main()

