
def get_haar_features(n, m):
    # Initialize a list to store the features
    features = []
    
    # Iterate over the input matrix
    for i in range(n):
        for j in range(m):
            # Check if the current element is white
            if matrix[i][j] == "W":
                # If it is white, add a new feature to the list
                features.append((i, j))
    
    # Return the list of features
    return features

def calculate_haar_feature(features, matrix):
    # Initialize a variable to store the sum of pixel values
    sum = 0
    
    # Iterate over the features
    for feature in features:
        # Calculate the sum of pixel values in the current feature
        sum += sum_pixels_in_feature(feature, matrix)
    
    # Return the sum
    return sum

def sum_pixels_in_feature(feature, matrix):
    # Initialize a variable to store the sum of pixel values
    sum = 0
    
    # Iterate over the pixels in the feature
    for i in range(feature[0], feature[2]):
        for j in range(feature[1], feature[3]):
            # Add the value of the current pixel to the sum
            sum += matrix[i][j]
    
    # Return the sum
    return sum

def main():
    # Read the input matrix
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(input()))
    
    # Get the Haar features
    features = get_haar_features(n, m)
    
    # Calculate the Haar feature
    sum = calculate_haar_feature(features, matrix)
    
    # Print the result
    print(sum)

if __name__ == '__main__':
    main()

