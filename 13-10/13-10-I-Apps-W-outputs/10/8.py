
def get_pointer_direction(step, directions):
    return directions[step - 1]

def get_next_step(step, direction):
    if direction == "U":
        return step + 1
    else:
        return step - 1

def get_duration(steps, directions):
    duration = 1
    current_step = 1
    while current_step <= steps:
        pointer_direction = get_pointer_direction(current_step, directions)
        next_step = get_next_step(current_step, pointer_direction)
        if next_step < 1 or next_step > steps:
            return -1
        current_step = next_step
        duration += 1
    return duration

def main():
    steps = int(input())
    directions = input()
    dream_duration = []
    for i in range(1, steps + 1):
        dream_duration.append(get_duration(steps, directions))
    print(*dream_duration)

if __name__ == '__main__':
    main()

