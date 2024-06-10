
def calculate_feature(n, m, feature):
    # Initialize variables
    value = 0
    operations = 0

    # Loop through each row of the feature
    for i in range(n):
        # Loop through each column of the feature
        for j in range(m):
            # If the current element of the feature is white, add the value of the corresponding pixel to the variable value
            if feature[i][j] == "W":
                value += 1
            # If the current element of the feature is black, subtract the value of the corresponding pixel from the variable value
            elif feature[i][j] == "B":
                value -= 1
        # After processing each row, add the value of the variable value to the total number of operations
        operations += value

    return operations

def main():
    # Read the input from stdin
    n, m = map(int, input().split())
    feature = []
    for i in range(n):
        feature.append(list(input()))

    # Calculate the feature value
    operations = calculate_feature(n, m, feature)

    # Print the result
    print(operations)

if __name__ == '__main__':
    main()

