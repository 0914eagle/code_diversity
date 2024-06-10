
def get_min_recorders(n, c, programs):
    recorders = []
    for program in sorted(programs, key=lambda x: x[0]):
        channel, start, end = program
        if not recorders or recorders[-1][1] < start:
            recorders.append([channel, end])
        else:
            recorders[-1][1] = max(recorders[-1][1], end)
    return len(recorders)

def main():
    n, c = map(int, input().split())
    programs = []
    for _ in range(n):
        s, t, c = map(int, input().split())
        programs.append([c, s, t])
    print(get_min_recorders(n, c, programs))

if __name__ == '__main__':
    main()

