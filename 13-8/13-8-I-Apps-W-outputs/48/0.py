
def get_min_moves(matrix, d):
    # Initialize the minimum number of moves to make all elements equal
    min_moves = 0
    # Initialize a set to store the unique elements in the matrix
    unique_elements = set()
    # Loop through each element in the matrix
    for row in matrix:
        for element in row:
            # Add the element to the set of unique elements
            unique_elements.add(element)
    # If there is only one unique element in the matrix, return -1
    if len(unique_elements) == 1:
        return -1
    # Loop through each element in the matrix
    for row in matrix:
        for element in row:
            # Find the difference between the element and the closest unique element
            diff = min(unique_elements, key=lambda x: abs(x - element))
            # If the difference is not zero, increment the minimum number of moves
            if diff != 0:
                min_moves += 1
    # Return the minimum number of moves
    return min_moves

def main():
    # Read the input n, m, and d
    n, m, d = map(int, input().split())
    # Read the matrix
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    # Find the minimum number of moves
    min_moves = get_min_moves(matrix, d)
    # Print the minimum number of moves
    print(min_moves)

if __name__ == '__main__':
    main()

