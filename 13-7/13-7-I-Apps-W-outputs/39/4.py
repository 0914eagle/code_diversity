
def get_feature_value(feature, image):
    # Initialize variables
    value = 0
    operations = 0
    
    # Loop through the feature and image
    for i in range(len(feature)):
        for j in range(len(feature[0])):
            # Check if the current pixel is white or black
            if feature[i][j] == "W":
                # Add the value of the pixel to the variable value
                value += image[i][j]
            else:
                # Subtract the value of the pixel from the variable value
                value -= image[i][j]
                
            # Increment the number of operations
            operations += 1
    
    # Return the value of the feature and the number of operations
    return value, operations

def main():
    # Read the input from stdin
    n, m = map(int, input().split())
    feature = [input() for _ in range(n)]
    image = [[int(j) for j in input().split()] for _ in range(n)]
    
    # Call the get_feature_value function
    value, operations = get_feature_value(feature, image)
    
    # Print the output
    print(operations)

if __name__ == '__main__':
    main()

