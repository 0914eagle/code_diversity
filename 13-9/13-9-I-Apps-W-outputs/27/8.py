
def can_reach_target(line, k):
    # Initialize variables
    current_position = line.index("G")
    target_position = line.index("T")
    visited = set()
    queue = []
    
    # Add the initial position to the queue
    queue.append(current_position)
    visited.add(current_position)
    
    # Loop through the queue
    while queue:
        current_position = queue.pop(0)
        
        # Check if the current position is the target position
        if current_position == target_position:
            return True
        
        # Add the neighbors to the queue
        for i in range(1, k + 1):
            neighbor = current_position + i
            if neighbor not in visited and neighbor < len(line) and line[neighbor] == ".":
                queue.append(neighbor)
                visited.add(neighbor)
    
    # If the queue is empty, return False
    return False

def main():
    n, k = map(int, input().split())
    line = input()
    if can_reach_target(line, k):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

