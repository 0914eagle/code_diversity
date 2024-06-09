
def spiral_order(matrix):
    if not matrix or not matrix[0]:
        return []
    m, n = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, m - 1, 0, n - 1
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction = directions[0]
    res = []
    for i in range(m * n):
        res.append(matrix[top][left])
        matrix[top][left] = 0
        if left == right or top == bottom:
            direction = directions[(directions.index(direction) + 1) % 4]
        top += direction[0]
        left += direction[1]
    return res

