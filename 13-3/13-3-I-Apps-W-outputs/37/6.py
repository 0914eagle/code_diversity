
def can_grasshopper_eat_insect(n, k, line):
    # Initialize the grasshopper's position and the target insect's position
    grasshopper_pos = line.index("G")
    insect_pos = line.index("T")
    
    # Check if the grasshopper's position is within the range of the line
    if grasshopper_pos < 0 or grasshopper_pos >= n:
        return "NO"
    
    # Check if the target insect's position is within the range of the line
    if insect_pos < 0 or insect_pos >= n:
        return "NO"
    
    # Check if the grasshopper can reach the target insect by jumping k cells at a time
    if abs(grasshopper_pos - insect_pos) > k:
        return "NO"
    
    # Check if the grasshopper can reach the target insect by jumping over obstacles
    for i in range(n):
        if line[i] == "#":
            continue
        if abs(grasshopper_pos - i) <= k and abs(insect_pos - i) <= k:
            return "YES"
    
    # If the grasshopper can't reach the target insect, return "NO"
    return "NO"

