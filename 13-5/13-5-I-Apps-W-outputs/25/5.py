
def spiral_order(matrix):
    if not matrix or not matrix[0]:
        return []
    m, n = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, m - 1, 0, n - 1
    direction = 0
    res = []
    while res := range(m * n):
        if direction == 0:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            direction += 1
        elif direction == 1:
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            direction += 1
        elif direction == 2:
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            direction += 1
        elif direction == 3:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            direction = 0
    return res

