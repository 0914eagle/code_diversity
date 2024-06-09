
def get_wrongness_sum(N, C, wrongness_matrix, colors):
    # Initialize the minimum sum of wrongness to infinity
    min_sum = float('inf')
    
    # Loop through all possible colors
    for color in range(1, C+1):
        # Initialize the current sum of wrongness to 0
        current_sum = 0
        
        # Loop through all squares
        for i in range(N):
            for j in range(N):
                # If the current color is not the same as the color of the square, add the wrongness to the current sum
                if colors[i][j] != color:
                    current_sum += wrongness_matrix[colors[i][j]][color]
        
        # If the current sum is less than the minimum sum, update the minimum sum
        if current_sum < min_sum:
            min_sum = current_sum
    
    # Return the minimum sum
    return min_sum

def main():
    # Read the input
    N, C = map(int, input().split())
    wrongness_matrix = []
    for i in range(C):
        wrongness_matrix.append(list(map(int, input().split())))
    colors = []
    for i in range(N):
        colors.append(list(map(int, input().split())))
    
    # Calculate the minimum sum of wrongness
    min_sum = get_wrongness_sum(N, C, wrongness_matrix, colors)
    
    # Print the minimum sum
    print(min_sum)

if __name__ == '__main__':
    main()

