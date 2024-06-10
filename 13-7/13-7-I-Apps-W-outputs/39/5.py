
def parse_input(n, m):
    # Parse the input feature matrix
    feature = []
    for _ in range(n):
        feature.append(input())
    return feature

def count_operations(feature):
    # Initialize variables
    n, m = len(feature), len(feature[0])
    operations = 0
    prefix_rectangles = []

    # Iterate over the rows of the feature matrix
    for i in range(n):
        # Iterate over the columns of the feature matrix
        for j in range(m):
            # If the current element is white, add a prefix rectangle with coefficient 1
            if feature[i][j] == "W":
                prefix_rectangles.append((i, j, 1))
            # If the current element is black, add a prefix rectangle with coefficient -1
            elif feature[i][j] == "B":
                prefix_rectangles.append((i, j, -1))

    # Sort the prefix rectangles by their y-coordinate in descending order
    prefix_rectangles.sort(key=lambda x: x[0], reverse=True)

    # Iterate over the prefix rectangles and count the number of operations required
    for i, j, coefficient in prefix_rectangles:
        operations += coefficient * (i + 1)

    return operations

def main():
    # Parse the input feature matrix
    n, m = map(int, input().split())
    feature = parse_input(n, m)

    # Count the number of operations required to calculate the feature
    operations = count_operations(feature)

    # Print the result
    print(operations)

if __name__ == '__main__':
    main()

