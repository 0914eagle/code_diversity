
def get_feature_value(image, feature):
    # Initialize variables
    value = 0
    operations = 0

    # Loop through the feature
    for i in range(len(feature)):
        for j in range(len(feature[0])):
            # If the feature cell is white, add the value of the image cell to the variable value
            if feature[i][j] == "W":
                value += image[i][j]
            # If the feature cell is black, subtract the value of the image cell from the variable value
            elif feature[i][j] == "B":
                value -= image[i][j]
            operations += 1

    return value, operations

def get_min_operations(feature):
    # Initialize variables
    min_operations = float("inf")
    value = 0

    # Loop through the feature
    for i in range(len(feature)):
        for j in range(len(feature[0])):
            # If the feature cell is white, add the value of the image cell to the variable value
            if feature[i][j] == "W":
                value += feature[i][j]
            # If the feature cell is black, subtract the value of the image cell from the variable value
            elif feature[i][j] == "B":
                value -= feature[i][j]
            min_operations = min(min_operations, value)

    return min_operations

def main():
    # Read the input
    n, m = map(int, input().split())
    feature = [input() for _ in range(n)]

    # Calculate the feature value and the minimum number of operations
    value, operations = get_feature_value(feature, feature)
    min_operations = get_min_operations(feature)

    # Print the result
    print(value)
    print(min_operations)

if __name__ == '__main__':
    main()

