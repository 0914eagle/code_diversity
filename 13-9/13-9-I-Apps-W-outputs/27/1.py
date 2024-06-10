
def is_jump_possible(n, k, line):
    # Initialize variables
    empty_cells = []
    obstacles = []
    grasshopper_position = 0
    insect_position = 0
    
    # Parse the input line
    for i, char in enumerate(line):
        if char == '.':
            empty_cells.append(i)
        elif char == '#':
            obstacles.append(i)
        elif char == 'G':
            grasshopper_position = i
        elif char == 'T':
            insect_position = i
    
    # Check if the grasshopper can reach the insect
    for i in range(len(empty_cells)):
        if empty_cells[i] - grasshopper_position == k:
            if empty_cells[i] == insect_position:
                return True
            elif empty_cells[i] in obstacles:
                break
    
    return False

def main():
    n, k = map(int, input().split())
    line = input()
    if is_jump_possible(n, k, line):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

