
def can_play_all_frequencies(freqs):
    # Initialize a list to store the intervals for each frequency
    intervals = []
    for freq in freqs:
        intervals.append([])
    # Iterate through the intervals for each frequency
    for i in range(len(freqs)):
        for j in range(0, len(freqs[i]), 2):
            # Check if the interval overlaps with any other interval
            for k in range(len(freqs)):
                if i != k:
                    for interval in intervals[k]:
                        if (freqs[i][j] <= interval[1] and freqs[i][j+1] >= interval[0]) or (freqs[i][j] >= interval[0] and freqs[i][j+1] <= interval[1]):
                            return "impossible"
            # Add the interval to the list of intervals for the current frequency
            intervals[i].append([freqs[i][j], freqs[i][j+1]])
    return "possible"

def main():
    freqs = []
    f = int(input())
    for i in range(f):
        t, n = map(int, input().split())
        freqs.append([t, n])
        for j in range(n):
            freqs[i].extend(map(int, input().split()))
    print(can_play_all_frequencies(freqs))

if __name__ == '__main__':
    main()

