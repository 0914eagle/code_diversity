
def find_largest_rectangle(matrix):
    # Initialize a list to store the heights of the bars
    heights = []
    
    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Loop through each column of the matrix
        for j in range(len(matrix[i])):
            # If the current element is 1, add its height to the list of heights
            if matrix[i][j] == "1":
                heights.append(int(matrix[i][j]))
            # If the current element is 0, add 0 to the list of heights
            else:
                heights.append(0)
    
    # Find the largest rectangle in the list of heights
    largest_rectangle = max(heights)
    
    return largest_rectangle

def main():
    # Test the function with the example matrix
    matrix = [
      ["1","0","1","0","0"],
      ["1","0","1","1","1"],
      ["1","1","1","1","1"],
      ["1","0","0","1","0"]
    ]
    largest_rectangle = find_largest_rectangle(matrix)
    print(largest_rectangle)

if __name__ == '__main__':
    main()

