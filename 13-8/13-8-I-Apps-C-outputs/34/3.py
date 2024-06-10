
def can_play_frequencies(frequencies):
    # Initialize a dictionary to store the playback times for each frequency
    playback_times = {}
    for frequency in frequencies:
        playback_times[frequency] = []

    # Iterate through the frequencies and add the playback times to the dictionary
    for frequency in frequencies:
        for playback_time in frequency[1]:
            playback_times[frequency[0]].append(playback_time)

    # Sort the playback times for each frequency in ascending order
    for frequency in playback_times:
        playback_times[frequency].sort()

    # Check if the playback times for each frequency are valid
    for frequency in playback_times:
        for i in range(len(playback_times[frequency]) - 1):
            if playback_times[frequency][i + 1] - playback_times[frequency][i] != frequency[1]:
                return "impossible"

    return "possible"

def main():
    frequencies = []
    for _ in range(int(input())):
        frequencies.append(list(map(int, input().split())))
    print(can_play_frequencies(frequencies))

if __name__ == '__main__':
    main()

