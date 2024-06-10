
def get_nearest_checkpoint(student_coords, checkpoint_coords):
    nearest_checkpoint = 0
    min_dist = float('inf')
    for i in range(len(checkpoint_coords)):
        dist = abs(student_coords[0] - checkpoint_coords[i][0]) + abs(student_coords[1] - checkpoint_coords[i][1])
        if dist < min_dist:
            min_dist = dist
            nearest_checkpoint = i + 1
    return nearest_checkpoint

def main():
    num_students, num_checkpoints = map(int, input().split())
    student_coords = []
    checkpoint_coords = []
    for i in range(num_students):
        student_coords.append(list(map(int, input().split())))
    for i in range(num_checkpoints):
        checkpoint_coords.append(list(map(int, input().split())))
    for student in student_coords:
        print(get_nearest_checkpoint(student, checkpoint_coords))

if __name__ == '__main__':
    main()

