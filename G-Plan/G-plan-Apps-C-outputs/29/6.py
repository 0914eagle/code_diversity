
def rotate_wheel(wheel, direction):
    if direction == 'left':
        return wheel[1:] + wheel[0]
    elif direction == 'right':
        return wheel[-1] + wheel[:-1]

def check_valid_configuration(wheels):
    for col in zip(*wheels):
        if len(set(col)) != 3:
            return False
    return True

def min_rotations(wheels):
    rotations = 0
    for i in range(len(wheels[0])):
        rotated_wheels = [rotate_wheel(wheel, 'left') for wheel in wheels]
        if check_valid_configuration(rotated_wheels):
            return rotations
        rotated_wheels = [rotate_wheel(wheel, 'right') for wheel in wheels]
        if check_valid_configuration(rotated_wheels):
            return rotations
        wheels = [rotate_wheel(wheel, 'right') for wheel in wheels]
        rotations += 1
    return -1

if __name__ == "__main__":
    wheel1 = input().strip()
    wheel2 = input().strip()
    wheel3 = input().strip()
    wheels = [wheel1, wheel2, wheel3]
    print(min_rotations(wheels))
