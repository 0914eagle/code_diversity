
def get_durations(n, s):
    # Initialize variables
    durations = [0] * n
    current_step = 0
    current_direction = 1
    time = 1

    # Iterate through the string
    for i in range(n):
        # Check if Olga moves beyond the stairs
        if current_step == 0 and s[i] == "D":
            durations[current_step] = -1
            break
        if current_step == n - 1 and s[i] == "U":
            durations[current_step] = -1
            break

        # Update the current step and direction
        current_step += current_direction
        if s[i] == "U":
            current_direction = 1
        else:
            current_direction = -1

        # Update the duration
        durations[current_step] = time
        time += 1

    return durations

def main():
    n = int(input())
    s = input()
    durations = get_durations(n, s)
    print(*durations, sep=" ")

if __name__ == '__main__':
    main()

