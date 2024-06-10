
def can_reach_insect(line, k):
    # Initialize variables
    empty_cells = []
    obstacle_cells = []
    grasshopper_cell = None
    insect_cell = None
    
    # Parse the line
    for i, char in enumerate(line):
        if char == '.':
            empty_cells.append(i)
        elif char == '#':
            obstacle_cells.append(i)
        elif char == 'G':
            grasshopper_cell = i
        elif char == 'T':
            insect_cell = i
    
    # Check if the grasshopper can reach the insect
    if grasshopper_cell is None or insect_cell is None:
        return "NO"
    if abs(grasshopper_cell - insect_cell) > k:
        return "NO"
    
    # Check if the grasshopper can make a jump to the insect
    jump_possible = False
    for cell in empty_cells:
        if abs(cell - grasshopper_cell) == k:
            jump_possible = True
            break
    
    if not jump_possible:
        return "NO"
    
    # Check if the grasshopper can make it through the obstacles
    for cell in obstacle_cells:
        if abs(cell - grasshopper_cell) <= k:
            return "NO"
    
    return "YES"

def main():
    n, k = map(int, input().split())
    line = input()
    print(can_reach_insect(line, k))

if __name__ == '__main__':
    main()

