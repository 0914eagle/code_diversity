
def spiral_order(matrix):
    if not matrix or not matrix[0]:
        return []
    m, n = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, m - 1, 0, n - 1
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_idx, res = 0, []
    while top <= bottom and left <= right:
        for _ in range(4):
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            for i in range(top + 1, bottom + 1):
                res.append(matrix[i][right])
            if top < bottom and left < right:
                for i in range(right - 1, left - 1, -1):
                    res.append(matrix[bottom][i])
                for i in range(bottom - 1, top, -1):
                    res.append(matrix[i][left])
        top += 1
        bottom -= 1
        left += 1
        right -= 1
        dir_idx = (dir_idx + 1) % 4
    return res

