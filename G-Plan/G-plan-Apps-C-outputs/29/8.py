te_wheel(wheel, direction):
    if direction == 'left':
        return wheel[1:] + wheel[0]
    elif direction == 'right':
        return wheel[-1] + wheel[:-1]

def check_valid_configuration(wheels):
    for col in zip(*wheels):
        if len(set(col)) != 3:
            return False
    return True

def min_rotations_required(wheels):
    for i in range(len(wheels[0])):
        rotated_wheels = [rotate_wheel(wheel, 'right') for wheel in wheels]
        if check_valid_configuration(rotated_wheels):
            return i + 1
        wheels = rotated_wheels
    return -1

if __name__ == "__main__":
    wheels = [input().strip() for _ in range(3)]
    print(min_rotations_required(wheels))
