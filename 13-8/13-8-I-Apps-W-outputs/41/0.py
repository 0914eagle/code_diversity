
def get_min_recorders(n, c, programs):
    recorders = []
    for program in sorted(programs, key=lambda x: x[0]):
        recorder_found = False
        for recorder in recorders:
            if recorder[0] == program[2] and recorder[1] <= program[0] < recorder[2]:
                recorder_found = True
                break
        if not recorder_found:
            recorders.append([program[2], program[0], program[1]])
    return len(recorders)

def main():
    n, c = map(int, input().split())
    programs = []
    for _ in range(n):
        s, t, c = map(int, input().split())
        programs.append([s, t, c])
    print(get_min_recorders(n, c, programs))

if __name__ == '__main__':
    main()

