
def can_grasshopper_reach_insect(line, k):
    # Initialize variables
    n = len(line)
    grasshopper_position = line.index("G")
    insect_position = line.index("T")
    visited = [False] * n
    
    # Base case: if the grasshopper is already at the insect's position, return True
    if grasshopper_position == insect_position:
        return True
    
    # Recursive case: try all possible jumps and check if the insect can be reached
    for i in range(1, k + 1):
        # Check if the jump is valid
        if grasshopper_position + i < n and line[grasshopper_position + i] != "#":
            # Mark the cell as visited
            visited[grasshopper_position + i] = True
            # Recursively call the function to check if the insect can be reached from the next cell
            if can_grasshopper_reach_insect(line, k):
                return True
            # Unmark the cell if the insect can't be reached from there
            visited[grasshopper_position + i] = False
    
    # If no jump leads to the insect, return False
    return False

def main():
    n, k = map(int, input().split())
    line = input()
    if can_grasshopper_reach_insect(line, k):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

