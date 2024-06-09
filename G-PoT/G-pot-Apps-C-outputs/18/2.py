
# Read input
r, c = map(int, input().split())
start_bed, fridge = eval(input()), eval(input())
school_map = [input() for _ in range(r)]
p = int(input())
patrol_paths = [list(map(eval, input().split())) for _ in range(p)]

# Define helper function to check if child can reach the fridge without being seen
def can_reach_fridge(turns):
    for path in patrol_paths:
        for i in range(len(path)):
            if i + turns >= len(path):
                break
            master_pos = path[i + turns]
            if master_pos[0] == child_pos[0] or master_pos[1] == child_pos[1]:
                return False
    return True

# Initialize variables
child_pos = start_bed
turns = 0

# Loop until child reaches the fridge or it's impossible to reach
while child_pos != fridge:
    turns += 1
    possible_moves = [(child_pos[0] + 1, child_pos[1]), (child_pos[0] - 1, child_pos[1]),
                      (child_pos[0], child_pos[1] + 1), (child_pos[0], child_pos[1] - 1)]
    valid_moves = [move for move in possible_moves if 0 <= move[0] < r and 0 <= move[1] < c and school_map[move[0]][move[1]] == '.']
    
    if not valid_moves:
        print("IMPOSSIBLE")
        break
    
    child_pos = valid_moves[0]
    
    if not can_reach_fridge(turns):
        print("IMPOSSIBLE")
        break

if child_pos == fridge:
    print(turns)
