
def is_playable(frequencies):
    # Initialize a dictionary to store the current position of the read/write head for each frequency
    head_positions = {}
    for frequency in frequencies:
        head_positions[frequency] = 0

    # Initialize a set to store the frequencies that are currently playing
    playing_frequencies = set()

    # Iterate through the intervals for each frequency
    for frequency, intervals in frequencies.items():
        for interval in intervals:
            # If the current position of the read/write head for this frequency is within the interval, play the frequency
            if head_positions[frequency] >= interval[0] and head_positions[frequency] <= interval[1]:
                playing_frequencies.add(frequency)
            # Otherwise, stop playing the frequency
            else:
                playing_frequencies.discard(frequency)

            # Update the position of the read/write head for this frequency
            head_positions[frequency] += 1

    # If all frequencies are playing, return "possible", otherwise return "impossible"
    if len(playing_frequencies) == len(frequencies):
        return "possible"
    else:
        return "impossible"

def main():
    f = int(input())
    frequencies = {}
    for _ in range(f):
        t, n = map(int, input().split())
        intervals = []
        for _ in range(n):
            t1, t2 = map(int, input().split())
            intervals.append((t1, t2))
        frequencies[t] = intervals
    print(is_playable(frequencies))

if __name__ == '__main__':
    main()

