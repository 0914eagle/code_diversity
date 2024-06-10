
def get_nearest_checkpoint(student_coords, checkpoint_coords):
    # Initialize the nearest checkpoint as the first checkpoint
    nearest_checkpoint = checkpoint_coords[0]
    nearest_dist = manhattan_dist(student_coords, nearest_checkpoint)

    # Loop through the remaining checkpoints and find the nearest one
    for checkpoint in checkpoint_coords[1:]:
        dist = manhattan_dist(student_coords, checkpoint)
        if dist < nearest_dist:
            nearest_checkpoint = checkpoint
            nearest_dist = dist

    return nearest_checkpoint

def manhattan_dist(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def get_student_checkpoints(student_coords, checkpoint_coords):
    student_checkpoints = []
    for student in student_coords:
        nearest_checkpoint = get_nearest_checkpoint(student, checkpoint_coords)
        student_checkpoints.append(nearest_checkpoint)

    return student_checkpoints

def main():
    student_coords, checkpoint_coords = read_input()
    student_checkpoints = get_student_checkpoints(student_coords, checkpoint_coords)
    for student_checkpoint in student_checkpoints:
        print(student_checkpoint)

def read_input():
    student_coords = []
    checkpoint_coords = []
    n, m = map(int, input().split())
    for i in range(n):
        a, b = map(int, input().split())
        student_coords.append((a, b))
    for i in range(m):
        c, d = map(int, input().split())
        checkpoint_coords.append((c, d))
    return student_coords, checkpoint_coords

if __name__ == '__main__':
    main()

