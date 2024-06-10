
def get_recorders(programs):
    recorders = []
    for program in sorted(programs, key=lambda x: x[1]):
        if not recorders or recorders[-1][1] < program[0]:
            recorders.append(program)
        else:
            recorders[-1][1] = max(recorders[-1][1], program[1])
    return len(recorders)

def main():
    num_programs, num_channels = map(int, input().split())
    programs = []
    for _ in range(num_programs):
        start, end, channel = map(int, input().split())
        programs.append((start, end, channel))
    print(get_recorders(programs))

if __name__ == '__main__':
    main()

