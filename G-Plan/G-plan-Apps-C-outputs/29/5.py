te_wheel_right(wheel):
    return wheel[-1] + wheel[:-1]

def rotate_wheel_left(wheel):
    return wheel[1:] + wheel[0]

def check_valid_configuration(wheels):
    for col in zip(*wheels):
        if len(set(col)) != 3:
            return False
    return True

def min_rotations_required(wheels):
    rotations = 0
    while not check_valid_configuration(wheels):
        wheels[0] = rotate_wheel_right(wheels[0])
        rotations += 1
        if rotations > len(wheels[0]):
            return -1
    return rotations

if __name__ == "__main__":
    wheels = [input().strip() for _ in range(3)]
    result = min_rotations_required(wheels)
    print(result)
