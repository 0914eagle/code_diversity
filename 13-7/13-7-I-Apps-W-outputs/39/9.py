
def calculate_haar_features(feature, image):
    # Initialize variables
    n, m = len(feature), len(feature[0])
    value = 0
    operations = 0

    # Loop through the feature table
    for i in range(n):
        for j in range(m):
            # Check if the current cell is white or black
            if feature[i][j] == "W":
                # Calculate the sum of pixels in the prefix rectangle with coefficient 1
                value += image[i][j]
                operations += 1
            else:
                # Calculate the sum of pixels in the prefix rectangle with coefficient -1
                value -= image[i][j]
                operations += 1

    return operations

def main():
    # Read the input
    n, m = map(int, input().split())
    feature = [input() for _ in range(n)]
    image = [input() for _ in range(n)]

    # Calculate the number of operations required to calculate the feature
    operations = calculate_haar_features(feature, image)

    # Print the result
    print(operations)

if __name__ == '__main__':
    main()

