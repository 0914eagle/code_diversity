
def get_squared_distance(matrix, row, col):
    # Find the index of the tree in the matrix
    tree_idx = next((i for i, x in enumerate(matrix[row]) if x == 'x'), None)
    
    # If there is no tree in the given row, return 0
    if tree_idx is None:
        return 0
    
    # Calculate the distance between the tree and the apple
    distance = abs(tree_idx - col)
    
    # Return the squared distance
    return distance ** 2

def main():
    # Read the input
    R, S = map(int, input().split())
    matrix = [input() for _ in range(R)]
    G = int(input())
    falls = [tuple(map(int, input().split())) for _ in range(G)]
    
    # Initialize the output list
    output = []
    
    # Iterate over the falls
    for fall in falls:
        # Get the squared distance for the current fall
        squared_distance = get_squared_distance(matrix, fall[0], fall[1])
        
        # Add the squared distance to the output list
        output.append(squared_distance)
    
    # Print the output
    print(*output, sep='\n')

if __name__ == '__main__':
    main()

