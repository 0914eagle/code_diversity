
def get_feature_value(feature, image):
    # Initialize variables
    value = 0
    operations = 0
    
    # Loop through the feature table
    for i in range(len(feature)):
        for j in range(len(feature[0])):
            # Check if the feature cell is white or black
            if feature[i][j] == "W":
                # Add the number of pixels in the prefix rectangle with the lower right corner in the i-th row and j-th column with coefficient 1 to the variable value
                value += image[i][j]
                operations += 1
            elif feature[i][j] == "B":
                # Add the number of pixels in the prefix rectangle with the lower right corner in the i-th row and j-th column with coefficient -1 to the variable value
                value -= image[i][j]
                operations += 1
    
    # Return the minimum number of operations required to calculate the feature value
    return operations

def main():
    # Read the feature table from stdin
    n, m = map(int, input().split())
    feature = []
    for _ in range(n):
        feature.append(list(input()))
    
    # Read the image from stdin
    image = []
    for _ in range(n):
        image.append(list(map(int, input().split())))
    
    # Calculate the feature value
    value = get_feature_value(feature, image)
    
    # Print the minimum number of operations required to calculate the feature value
    print(value)

if __name__ == '__main__':
    main()

