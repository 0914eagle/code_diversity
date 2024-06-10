
def get_min_recorders(n, c, programs):
    recorders = []
    for program in sorted(programs, key=lambda x: x[2]):
        channel, start, end = program
        recorder_index = None
        for i, recorder in enumerate(recorders):
            if recorder[0] == channel:
                recorder_index = i
                break
        if recorder_index is None:
            recorder_index = len(recorders)
            recorders.append([channel, start, end])
        else:
            recorder = recorders[recorder_index]
            if recorder[1] > start:
                recorder[1] = start
            if recorder[2] < end:
                recorder[2] = end
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

