
def check_pauses(intervals):
    for i in range(len(intervals) - 1):
        if intervals[i + 1][0] - intervals[i][1] != 1:
            return False
    return True

def check_frequencies(frequencies):
    for frequency in frequencies:
        if not check_pauses(frequency[1]):
            return False
    return True

def main():
    num_frequencies = int(input())
    frequencies = []
    for i in range(num_frequencies):
        t, n = map(int, input().split())
        intervals = []
        for j in range(n):
            t1, t2 = map(int, input().split())
            intervals.append([t1, t2])
        frequencies.append([t, intervals])
    if check_frequencies(frequencies):
        print("possible")
    else:
        print("impossible")

if __name__ == '__main__':
    main()

