
def get_haar_feature_value(feature, image):
    # Initialize variables
    value = 0
    operations = 0
    
    # Loop through each row of the feature
    for i in range(len(feature)):
        # Loop through each column of the feature
        for j in range(len(feature[i])):
            # Check if the current cell is white or black
            if feature[i][j] == "W":
                # Add the sum of pixels in the prefix rectangle with the lower right corner in the current row and column with coefficient 1 to the variable value
                value += image[i][j]
                operations += 1
            elif feature[i][j] == "B":
                # Add the number of pixels in the prefix rectangle with the lower right corner in the current row and column with coefficient -1 and variable value
                value -= image[i][j]
                operations += 1
    
    # Return the minimum number of operations required to calculate the value of the feature
    return operations

def main():
    # Read the input feature
    n, m = map(int, input().split())
    feature = []
    for i in range(n):
        feature.append(list(input()))
    
    # Read the input image
    image = []
    for i in range(n):
        image.append([int(x) for x in input().split()])
    
    # Calculate the minimum number of operations required to calculate the value of the feature
    value = get_haar_feature_value(feature, image)
    
    # Print the result
    print(value)

if __name__ == '__main__':
    main()

