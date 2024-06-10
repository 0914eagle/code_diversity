
def calculate_haar_features(feature, image):
    # Initialize variables
    n, m = len(feature), len(feature[0])
    value = 0
    operations = 0

    # Iterate over the feature
    for i in range(n):
        for j in range(m):
            # If the current element of the feature is white, add the sum of pixels in the prefix rectangle with the lower right corner in the i-th row and j-th column with coefficient 1 to the variable value
            if feature[i][j] == "W":
                value += sum(image[i:n, j:j+1])
                operations += 1
            # If the current element of the feature is black, add the number of pixels in the prefix rectangle with the lower right corner in the i-th row and j-th column with coefficient -1 and variable value
            elif feature[i][j] == "B":
                value += len(image[i:n, j:j+1])
                operations += 1

    return operations

def main():
    # Read input
    n, m = map(int, input().split())
    feature = [input() for _ in range(n)]
    image = [[1 for _ in range(m)] for _ in range(n)]

    # Calculate the minimum number of operations required to calculate the values of the feature
    operations = calculate_haar_features(feature, image)

    # Print output
    print(operations)

if __name__ == '__main__':
    main()

