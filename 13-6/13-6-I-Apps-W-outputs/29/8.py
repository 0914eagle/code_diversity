
def get_wrongness_sum(N, C, wrongness, colors):
    # Initialize the minimum sum of wrongness to infinity
    min_sum = float('inf')
    
    # Loop through all possible colors
    for color in range(1, C+1):
        # Initialize the current sum of wrongness to zero
        current_sum = 0
        
        # Loop through all squares
        for i in range(N):
            for j in range(N):
                # If the current color is the same as the color of the square
                if colors[i][j] == color:
                    # Add the wrongness of the square to the current sum
                    current_sum += wrongness[i][j]
        
        # If the current sum is less than the minimum sum, update the minimum sum
        if current_sum < min_sum:
            min_sum = current_sum
    
    # Return the minimum sum of wrongness
    return min_sum

def main():
    # Read the input data
    N, C = map(int, input().split())
    wrongness = []
    colors = []
    for i in range(N):
        wrongness.append(list(map(int, input().split())))
        colors.append(list(map(int, input().split())))
    
    # Get the minimum sum of wrongness
    min_sum = get_wrongness_sum(N, C, wrongness, colors)
    
    # Print the minimum sum of wrongness
    print(min_sum)

if __name__ == '__main__':
    main()

