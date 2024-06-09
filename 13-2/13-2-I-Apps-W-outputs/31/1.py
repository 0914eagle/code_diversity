
def max_rectangle_area(matrix):
    # Initialize variables
    max_area = 0
    rows = len(matrix)
    cols = len(matrix[0])
    top_down_traversal = [0] * cols
    left_right_traversal = [0] * cols

    # Traverse each row
    for i in range(rows):
        # Traverse each column
        for j in range(cols):
            # If the current cell is 1, increment the top-down and left-right traversals
            if matrix[i][j] == "1":
                top_down_traversal[j] += 1
                left_right_traversal[j] += 1
            # If the current cell is 0, reset the top-down traversal
            else:
                top_down_traversal[j] = 0

        # Update the maximum area
        max_area = max(max_area, max_rectangle_in_top_down_traversal(top_down_traversal))

    # Traverse each column
    for j in range(cols):
        # Traverse each row
        for i in range(rows):
            # If the current cell is 1, increment the left-right traversal
            if matrix[i][j] == "1":
                left_right_traversal[j] += 1
            # If the current cell is 0, reset the left-right traversal
            else:
                left_right_traversal[j] = 0

        # Update the maximum area
        max_area = max(max_area, max_rectangle_in_left_right_traversal(left_right_traversal))

    return max_area

# Find the maximum rectangle in a top-down traversal
def max_rectangle_in_top_down_traversal(top_down_traversal):
    # Initialize variables
    max_area = 0
    stack = []

    # Traverse the traversal
    for i in range(len(top_down_traversal)):
        # If the current element is 0, pop elements from the stack
        while stack and top_down_traversal[i] < top_down_traversal[stack[-1]]:
            h = top_down_traversal[stack.pop()]
            w = i - stack[-1] - 1
            max_area = max(max_area, h * w)
        # Push the current element onto the stack
        stack.append(i)

    # Pop all the remaining elements from the stack
    while stack:
        h = top_down_traversal[stack.pop()]
        w = len(top_down_traversal) - stack[-1] - 1
        max_area = max(max_area, h * w)

    return max_area

# Find the maximum rectangle in a left-right traversal
def max_rectangle_in_left_right_traversal(left_right_traversal):
    # Initialize variables
    max_area = 0
    stack = []

    # Traverse the traversal
    for i in range(len(left_right_traversal)):
        # If the current element is 0, pop elements from the stack
        while stack and left_right_traversal[i] < left_right_traversal[stack[-1]]:
            h = left_right_traversal[stack.pop()]
            w = i - stack[-1] - 1
            max_area = max(max_area, h * w)
        # Push the current element onto the stack
        stack.append(i)

    # Pop all the remaining elements from the stack
    while stack:
        h = left_right_traversal[stack.pop()]
        w = len(left_right_traversal) - stack[-1] - 1
        max_area = max(max_area, h * w)

    return max_area

