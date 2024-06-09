
def get_squared_distance(r1, s1, r2, s2):
    return (r1-r2)**2 + (s1-s2)**2

def solve(matrix, falls):
    distances = []
    for fall in falls:
        row, col = fall
        distance = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'x' and (i != row or j != col):
                    distance += get_squared_distance(i, j, row, col)
        distances.append(distance)
    return distances

