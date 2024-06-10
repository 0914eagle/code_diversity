te_wheel(wheel, direction):
    if direction == 'right':
        return wheel[-1] + wheel[:-1]
    elif direction == 'left':
        return wheel[1:] + wheel[0]

def check_valid_configuration(wheels):
    for col in zip(*wheels):
        if len(set(col)) != 3:
            return False
    return True

def min_rotations_required(wheels):
    min_rotations = float('inf')
    for i in range(len(wheels[0])):
        rotations = i
        temp_wheels = [wheel[:] for wheel in wheels]
        for j in range(3):
            if check_valid_configuration(temp_wheels):
                min_rotations = min(min_rotations, rotations)
            temp_wheels = [rotate_wheel(wheel, 'right') for wheel in temp_wheels]
        wheels = [rotate_wheel(wheel, 'left') for wheel in wheels]
    return min_rotations if min_rotations != float('inf') else -1

if __name__ == "__main__":
    wheels = [input().strip() for _ in range(3)]
    print(min_rotations_required(wheels))
