
def find_largest_rectangle(matrix):
    # Initialize a list to store the heights of the bars
    heights = [0] * len(matrix[0])
    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Loop through each column of the row
        for j in range(len(matrix[i])):
            # If the current element is 1, increment the height
            if matrix[i][j] == "1":
                heights[j] += 1
            # If the current element is 0, set the height to 0
            else:
                heights[j] = 0
    # Find the largest rectangle by traversing the heights list and calculating the area of each rectangle
    largest_rectangle = 0
    for i in range(len(heights)):
        # Initialize the current area to 0
        current_area = 0
        # Loop through each element in the heights list from the current index to the end
        for j in range(i, len(heights)):
            # Update the current area by adding the current height to the previous area
            current_area += heights[j]
            # If the current area is greater than the largest area, update the largest area
            if current_area > largest_rectangle:
                largest_rectangle = current_area
    return largest_rectangle

def input_matrix():
    # Input the number of rows and columns in the matrix
    rows, cols = map(int, input("Enter the number of rows and columns: ").split())
    # Initialize a list to store the matrix
    matrix = []
    # Loop through each row of the matrix
    for i in range(rows):
        # Input a list of integers for the current row
        matrix.append(list(map(int, input("Enter a row: ").split())))
    return matrix

if __name__ == '__main__':
    # Get the matrix from the user
    matrix = input_matrix()
    # Find the largest rectangle in the matrix
    largest_rectangle = find_largest_rectangle(matrix)
    # Print the largest rectangle
    print(f"The largest rectangle in the matrix is: {largest_rectangle}")

