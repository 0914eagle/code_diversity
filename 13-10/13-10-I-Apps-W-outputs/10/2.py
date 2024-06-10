
def get_dream_duration(n, s):
    durations = []
    for i in range(n):
        if s[i] == "U":
            durations.append(i + 1)
        else:
            durations.append(n - i)
    return durations

def get_steps_beyond_stairs(n, s):
    steps_beyond_stairs = []
    for i in range(n):
        if s[i] == "U" and i == 0:
            steps_beyond_stairs.append(1)
        elif s[i] == "D" and i == n - 1:
            steps_beyond_stairs.append(1)
        else:
            steps_beyond_stairs.append(0)
    return steps_beyond_stairs

def get_dream_durations(n, s):
    durations = get_dream_duration(n, s)
    steps_beyond_stairs = get_steps_beyond_stairs(n, s)
    for i in range(n):
        if steps_beyond_stairs[i] == 1:
            durations[i] = -1
    return durations

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(*get_dream_durations(n, s), sep=' ')

