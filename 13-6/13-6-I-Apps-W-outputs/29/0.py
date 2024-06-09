
def read_input():
    N, C = map(int, input().split())
    D = []
    for i in range(C):
        D.append(list(map(int, input().split())))
    c = []
    for i in range(N):
        c.append(list(map(int, input().split())))
    return N, C, D, c

def solve(N, C, D, c):
    # Initialize the minimum sum of wrongness to infinity
    min_sum = float('inf')
    # Loop through all possible colors
    for color in range(1, C+1):
        # Initialize the sum of wrongness for this color to 0
        sum_wrongness = 0
        # Loop through all squares
        for i in range(N):
            for j in range(N):
                # If the current square is not the same color as the target color
                if c[i][j] != color:
                    # Add the wrongness of the square to the sum
                    sum_wrongness += D[c[i][j]-1][color-1]
        # If the sum of wrongness for this color is less than the minimum sum, update the minimum sum
        if sum_wrongness < min_sum:
            min_sum = sum_wrongness
    # Return the minimum sum of wrongness
    return min_sum

def main():
    N, C, D, c = read_input()
    print(solve(N, C, D, c))

if __name__ == '__main__':
    main()

