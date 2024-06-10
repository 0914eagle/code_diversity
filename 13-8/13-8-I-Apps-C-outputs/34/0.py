
def play_movie_theme_songs(frequencies):
    # Initialize a dictionary to store the frequencies and their intervals
    frequency_intervals = {}
    for frequency in frequencies:
        frequency_intervals[frequency] = []

    # Iterate over the intervals for each frequency
    for frequency in frequencies:
        for interval in frequency_intervals[frequency]:
            # Check if the interval is valid
            if interval[1] - interval[0] != 1:
                return "impossible"

    # If all intervals are valid, return "possible"
    return "possible"

def main():
    frequencies = []
    for _ in range(int(input())):
        t, n = map(int, input().split())
        intervals = []
        for _ in range(n):
            intervals.append(list(map(int, input().split())))
        frequencies.append((t, intervals))
    print(play_movie_theme_songs(frequencies))

if __name__ == '__main__':
    main()

