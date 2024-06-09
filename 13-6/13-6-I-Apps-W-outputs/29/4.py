
def get_wrongness_sum(N, C, D, c):
    # Initialize the wrongness sum to 0
    wrongness_sum = 0
    
    # Loop through each square
    for i in range(N):
        for j in range(N):
            # Get the current color of the square
            current_color = c[i][j]
            
            # Loop through each adjacent square
            for x in range(N):
                for y in range(N):
                    # Check if the current square and the adjacent square have the same color
                    if current_color == c[x][y]:
                        # Add the wrongness of the current square and the adjacent square to the sum
                        wrongness_sum += D[current_color - 1][c[x][y] - 1]
    
    # Return the wrongness sum
    return wrongness_sum

def solve(N, C, D, c):
    # Initialize the minimum wrongness sum to infinity
    min_wrongness_sum = float('inf')
    
    # Loop through each possible color
    for color in range(1, C + 1):
        # Create a copy of the current color grid
        new_c = [[0] * N for _ in range(N)]
        
        # Loop through each square
        for i in range(N):
            for j in range(N):
                # If the current square is not the color we are trying to change it to, change it
                if c[i][j] != color:
                    new_c[i][j] = color
        
        # Get the wrongness sum of the new color grid
        wrongness_sum = get_wrongness_sum(N, C, D, new_c)
        
        # Check if the wrongness sum is less than the minimum wrongness sum
        if wrongness_sum < min_wrongness_sum:
            # Update the minimum wrongness sum
            min_wrongness_sum = wrongness_sum
    
    # Return the minimum wrongness sum
    return min_wrongness_sum

if __name__ == '__main__':
    # Read the input
    N, C = map(int, input().split())
    D = []
    for i in range(C):
        D.append(list(map(int, input().split())))
    c = []
    for i in range(N):
        c.append(list(map(int, input().split())))
    
    # Solve the problem
    print(solve(N, C, D, c))

