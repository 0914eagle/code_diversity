
def max_rectangle_area(matrix):
    def largest_rectangle_in_rectangle(heights):
        max_area = 0
        stack = [-1]
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                max_area = max(max_area, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        while stack[-1] != -1:
            max_area = max(max_area, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return max_area

    max_area = 0
    for i in range(len(matrix)):
        heights = [0] * len(matrix[0])
        for j in range(len(matrix[0])):
            heights[j] = heights[j] + 1 if matrix[i][j] == "1" else 0
        max_area = max(max_area, largest_rectangle_in_rectangle(heights))
    return max_area

