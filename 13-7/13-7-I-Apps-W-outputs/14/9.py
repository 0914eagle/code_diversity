
def get_min_mp_cost(c_matrix, wall_matrix):
    # Initialize the minimum MP cost to turn every digit into 1 as infinity
    min_mp_cost = float('inf')
    
    # Loop through every possible digit that can be turned into 1
    for digit in range(10):
        # If the current digit is not present on the wall, skip it
        if digit not in wall_matrix:
            continue
        
        # Get the current MP cost to turn the current digit into 1
        mp_cost = get_mp_cost(c_matrix, wall_matrix, digit)
        
        # If the current MP cost is less than the minimum MP cost, update the minimum MP cost
        if mp_cost < min_mp_cost:
            min_mp_cost = mp_cost
    
    return min_mp_cost

def get_mp_cost(c_matrix, wall_matrix, digit):
    # Initialize the current MP cost to 0
    mp_cost = 0
    
    # Loop through every square on the wall
    for i in range(len(wall_matrix)):
        for j in range(len(wall_matrix[0])):
            # If the current square contains the current digit, add the MP cost to turn it into 1
            if wall_matrix[i][j] == digit:
                mp_cost += c_matrix[digit][1]
    
    return mp_cost

def main():
    # Read the input from stdin
    h, w = map(int, input().split())
    c_matrix = [list(map(int, input().split())) for _ in range(10)]
    wall_matrix = [list(map(int, input().split())) for _ in range(h)]
    
    # Get the minimum MP cost to turn every digit on the wall into 1
    min_mp_cost = get_min_mp_cost(c_matrix, wall_matrix)
    
    # Print the minimum MP cost
    print(min_mp_cost)

if __name__ == '__main__':
    main()

