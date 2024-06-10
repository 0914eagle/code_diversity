
def can_grasshopper_jump(n, k, line):
    # Initialize the grasshopper's position and the target insect's position
    grasshopper_pos = line.index("G")
    target_pos = line.index("T")
    
    # Initialize a set to keep track of the visited cells
    visited = set()
    
    # Initialize a queue to keep track of the cells to visit
    queue = [grasshopper_pos]
    
    # Loop until the queue is empty
    while queue:
        # Get the current cell from the queue
        current_pos = queue.pop(0)
        
        # If the current cell is the target cell, return True
        if current_pos == target_pos:
            return True
        
        # If the current cell has already been visited, skip it
        if current_pos in visited:
            continue
        
        # Mark the current cell as visited
        visited.add(current_pos)
        
        # Get the neighbors of the current cell
        neighbors = [current_pos + i for i in range(-k, k + 1) if i != 0 and 0 <= current_pos + i < n and line[current_pos + i] != '#']
        
        # Add the neighbors to the queue
        queue += neighbors
    
    # If the queue is empty and the target cell has not been visited, return False
    return False

def main():
    n, k = map(int, input().split())
    line = list(input())
    print("YES" if can_grasshopper_jump(n, k, line) else "NO")

if __name__ == '__main__':
    main()

