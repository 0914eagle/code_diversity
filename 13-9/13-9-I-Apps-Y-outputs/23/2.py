
def get_manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def get_nearest_checkpoint(student_coordinates, checkpoint_coordinates):
    nearest_checkpoint = None
    min_distance = float('inf')
    for i in range(len(checkpoint_coordinates)):
        distance = get_manhattan_distance(student_coordinates[0], student_coordinates[1], checkpoint_coordinates[i][0], checkpoint_coordinates[i][1])
        if distance < min_distance:
            min_distance = distance
            nearest_checkpoint = i
    return nearest_checkpoint

def solve(student_coordinates, checkpoint_coordinates):
    return [get_nearest_checkpoint(student_coordinates[i], checkpoint_coordinates) for i in range(len(student_coordinates))]

if __name__ == '__main__':
    student_coordinates = []
    checkpoint_coordinates = []
    n, m = map(int, input().split())
    for i in range(n):
        student_coordinates.append(list(map(int, input().split())))
    for i in range(m):
        checkpoint_coordinates.append(list(map(int, input().split())))
    result = solve(student_coordinates, checkpoint_coordinates)
    for i in range(n):
        print(result[i] + 1)

