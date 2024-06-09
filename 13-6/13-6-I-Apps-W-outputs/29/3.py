
def get_wrongness_sum(N, C, D, c):
    # Initialize the wrongness sum to 0
    wrongness_sum = 0
    
    # Loop through each row
    for i in range(N):
        # Loop through each column
        for j in range(N):
            # Check if the current square is the same color as the square above it
            if c[i][j] == c[i-1][j]:
                # Add the wrongness of the current square to the sum
                wrongness_sum += D[c[i][j]][c[i-1][j]]
    
    # Loop through each column
    for j in range(N):
        # Loop through each row
        for i in range(N):
            # Check if the current square is the same color as the square to the left of it
            if c[i][j] == c[i][j-1]:
                # Add the wrongness of the current square to the sum
                wrongness_sum += D[c[i][j]][c[i][j-1]]
    
    # Return the wrongness sum
    return wrongness_sum

def solve(N, C, D, c):
    # Initialize the minimum wrongness sum to infinity
    min_wrongness_sum = float('inf')
    
    # Loop through each row
    for i in range(N):
        # Loop through each column
        for j in range(N):
            # Loop through each color
            for k in range(C):
                # Check if the current square is not the same color as the square above it or to the left of it
                if c[i][j] != c[i-1][j] and c[i][j] != c[i][j-1]:
                    # Repaint the current square to the current color
                    c[i][j] = k
                    # Calculate the wrongness sum of the new grid
                    wrongness_sum = get_wrongness_sum(N, C, D, c)
                    # Check if the wrongness sum is less than the minimum wrongness sum
                    if wrongness_sum < min_wrongness_sum:
                        # Update the minimum wrongness sum
                        min_wrongness_sum = wrongness_sum
    
    # Return the minimum wrongness sum
    return min_wrongness_sum

if __name__ == '__main__':
    N, C = map(int, input().split())
    D = []
    for i in range(C):
        D.append(list(map(int, input().split())))
    c = []
    for i in range(N):
        c.append(list(map(int, input().split())))
    print(solve(N, C, D, c))

