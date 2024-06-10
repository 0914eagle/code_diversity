
def rotate_wheel(wheel, direction):
    if direction == 'right':
        return wheel[-1] + wheel[:-1]
    elif direction == 'left':
        return wheel[1:] + wheel[0]

def check_valid_configuration(wheels):
    for i in range(len(wheels[0])):
        letters = set()
        for wheel in wheels:
            letters.add(wheel[i])
        if len(letters) != 3:
            return False
    return True

def min_rotations_required(wheels):
    min_rotations = float('inf')
    for i in range(len(wheels[0])):
        rotations = 0
        temp_wheels = [wheel[:] for wheel in wheels]
        while not check_valid_configuration(temp_wheels):
            for j in range(3):
                temp_wheels[j] = rotate_wheel(temp_wheels[j], 'right')
            rotations += 1
        min_rotations = min(min_rotations, rotations)
    return min_rotations if min_rotations != float('inf') else -1

if __name__ == "__main__":
    wheels = [input().strip() for _ in range(3)]
    print(min_rotations_required(wheels))
