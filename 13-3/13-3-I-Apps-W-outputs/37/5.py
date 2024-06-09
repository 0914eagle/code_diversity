
def can_grasshopper_eat_insect(n, k, line):
    # Initialize the grasshopper's position and the insect's position
    grasshopper_pos = line.index("G")
    insect_pos = line.index("T")
    
    # Check if the grasshopper's position is within the bounds of the line
    if grasshopper_pos < 0 or grasshopper_pos >= n:
        return "NO"
    
    # Check if the insect's position is within the bounds of the line
    if insect_pos < 0 or insect_pos >= n:
        return "NO"
    
    # Check if the grasshopper can reach the insect in one jump
    if abs(grasshopper_pos - insect_pos) <= k:
        return "YES"
    
    # Check if the grasshopper can reach the insect by jumping over obstacles
    for i in range(n):
        # Check if the current cell is an obstacle
        if line[i] == "#":
            continue
        
        # Check if the grasshopper can jump to the current cell from the previous cell
        if i - grasshopper_pos == k or grasshopper_pos - i == k:
            # Update the grasshopper's position and check if it matches the insect's position
            grasshopper_pos = i
            if grasshopper_pos == insect_pos:
                return "YES"
    
    # If the grasshopper couldn't reach the insect, return "NO"
    return "NO"

