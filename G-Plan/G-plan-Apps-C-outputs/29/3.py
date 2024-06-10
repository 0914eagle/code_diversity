te_wheel_right(wheel):
    return wheel[-1] + wheel[:-1]

def rotate_wheel_left(wheel):
    return wheel[1:] + wheel[0]

def check_valid_configuration(wheel1, wheel2, wheel3):
    for i in range(len(wheel1)):
        if wheel1[i] == wheel2[i] or wheel1[i] == wheel3[i] or wheel2[i] == wheel3[i]:
            return False
    return True

def find_minimum_rotations(wheel1, wheel2, wheel3):
    rotations = 0
    for _ in range(len(wheel1)):
        if check_valid_configuration(wheel1, wheel2, wheel3):
            return rotations
        wheel1 = rotate_wheel_right(wheel1)
        rotations += 1
    return -1

if __name__ == "__main__":
    wheel1 = input().strip()
    wheel2 = input().strip()
    wheel3 = input().strip()
    
    result = find_minimum_rotations(wheel1, wheel2, wheel3)
    print(result)
