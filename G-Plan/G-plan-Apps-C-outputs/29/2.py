
def rotate_wheel_right(wheel):
    return wheel[-1] + wheel[:-1]

def rotate_wheel_left(wheel):
    return wheel[1:] + wheel[0]

def check_valid_configuration(wheels):
    for col in zip(*wheels):
        if len(set(col)) != 3:
            return False
    return True

def min_rotations(wheels):
    for i in range(len(wheels[0])):
        if check_valid_configuration(wheels):
            return i
        wheels = [rotate_wheel_right(wheel) for wheel in wheels]
    return -1

if __name__ == "__main__":
    wheels = [input().strip() for _ in range(3)]
    print(min_rotations(wheels))
