
def get_nearest_checkpoint(student_x, student_y, checkpoint_x, checkpoint_y):
    return abs(student_x - checkpoint_x) + abs(student_y - checkpoint_y)

def get_nearest_checkpoint_index(student_x, student_y, checkpoint_x, checkpoint_y, checkpoint_index):
    return checkpoint_index, get_nearest_checkpoint(student_x, student_y, checkpoint_x, checkpoint_y)

def get_nearest_checkpoints(student_x, student_y, checkpoints):
    nearest_checkpoints = []
    for checkpoint in checkpoints:
        nearest_checkpoints.append(get_nearest_checkpoint_index(student_x, student_y, *checkpoint))
    nearest_checkpoints = sorted(nearest_checkpoints, key=lambda x: x[1])
    return nearest_checkpoints

def solve(student_coordinates, checkpoint_coordinates):
    nearest_checkpoints = []
    for student in student_coordinates:
        nearest_checkpoints.append(get_nearest_checkpoints(student[0], student[1], checkpoint_coordinates))
    return [nearest_checkpoints[i][0][0] for i in range(len(nearest_checkpoints))]

if __name__ == '__main__':
    student_coordinates = []
    checkpoint_coordinates = []
    for _ in range(int(input())):
        student_coordinates.append(list(map(int, input().split())))
    for _ in range(int(input())):
        checkpoint_coordinates.append(list(map(int, input().split())))
    print(*solve(student_coordinates, checkpoint_coordinates), sep='\n')

