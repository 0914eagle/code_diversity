
def max_rectangle_area(matrix):
    # Initialize the result and the heights array
    result = 0
    heights = [0] * len(matrix[0])

    # Loop through each row
    for i in range(len(matrix)):
        # Loop through each column
        for j in range(len(matrix[i])):
            # If the current cell is 1, update the height
            if matrix[i][j] == "1":
                heights[j] += 1
            # If the current cell is 0, update the height to 0
            else:
                heights[j] = 0

        # Update the result using the largest rectangle in the current row
        result = max(result, largest_rectangle(heights))

    return result

# Function to find the largest rectangle in a histogram
def largest_rectangle(heights):
    # Initialize the result and the stack
    result = 0
    stack = [-1]

    # Loop through the heights
    for i in range(len(heights)):
        # While the top of the stack is not -1 and the current height is less than the stack top, pop the stack
        while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
            top = stack.pop()
            result = max(result, heights[top] * (i - stack[-1] - 1))

        # Push the current index to the stack
        stack.append(i)

    # If the stack is not empty, there is at least one rectangle, so return the result
    if stack[0] != -1:
        return result

    # If the stack is empty, there are no rectangles, so return 0
    return 0

