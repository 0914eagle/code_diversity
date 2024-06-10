
def solve_query(n, m, c_l, c_e, v, q, x_1, y_1, x_2, y_2):
    # Initialize the grid
    grid = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Fill in the stairs
    for i in range(c_l):
        grid[l_i][l_i] = 1
    
    # Fill in the elevators
    for i in range(c_e):
        grid[e_i][e_i] = 1
    
    # Fill in the rest of the grid
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                grid[i][j] = 1
    
    # Calculate the minimum time needed to go from (x_1, y_1) to (x_2, y_2)
    time = 0
    current_floor = x_1
    current_section = y_1
    while current_floor != x_2 or current_section != y_2:
        # Check if the next step is an elevator or a stair
        if current_floor == x_2 or current_section == y_2:
            next_floor = current_floor
            next_section = current_section
        elif grid[current_floor][current_section] == 1:
            next_floor = current_floor
            next_section = current_section
        elif grid[current_floor][current_section] == 2:
            next_floor = current_floor + 1
            next_section = current_section
        else:
            next_floor = current_floor - 1
            next_section = current_section
        
        # Calculate the time needed to move to the next floor
        if next_floor == current_floor:
            time += 1
        elif abs(next_floor - current_floor) == 1:
            time += 1
        else:
            time += v
        
        # Update the current floor and section
        current_floor = next_floor
        current_section = next_section
    
    return time

def main():
    n, m, c_l, c_e, v = map(int, input().split())
    l = list(map(int, input().split()))
    e = list(map(int, input().split()))
    q = int(input())
    
    for _ in range(q):
        x_1, y_1, x_2, y_2 = map(int, input().split())
        print(solve_query(n, m, c_l, c_e, v, q, x_1, y_1, x_2, y_2))

if __name__ == '__main__':
    main()

