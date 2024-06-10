
def get_min_recorders(N, C, programs):
    recorders = []
    for program in sorted(programs, key=lambda x: x[1]):
        channel, start, end = program[0], program[1], program[2]
        if not recorders or recorders[-1][0] != channel:
            recorders.append([channel, start, end])
        else:
            recorders[-1][1] = min(recorders[-1][1], start)
            recorders[-1][2] = max(recorders[-1][2], end)

    return len(recorders)

def main():
    N, C = map(int, input().split())
    programs = []
    for _ in range(N):
        s, t, c = map(int, input().split())
        programs.append([c, s, t])
    print(get_min_recorders(N, C, programs))

if __name__ == '__main__':
    main()

