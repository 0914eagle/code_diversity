
def can_play_music(frequencies):
    # Initialize a dictionary to store the frequency and its corresponding intervals
    frequency_intervals = {}
    for frequency in frequencies:
        frequency_intervals[frequency] = []

    # Iterate through the intervals for each frequency
    for frequency in frequencies:
        for interval in frequency_intervals[frequency]:
            # Check if the interval overlaps with any of the other intervals
            for other_frequency in frequency_intervals:
                if other_frequency != frequency:
                    for other_interval in frequency_intervals[other_frequency]:
                        if do_intervals_overlap(interval, other_interval):
                            return "impossible"

    # If all intervals can be played without overlapping, return "possible"
    return "possible"

def do_intervals_overlap(interval1, interval2):
    # Check if the intervals overlap by comparing their start and end times
    return not (interval1[1] <= interval2[0] or interval2[1] <= interval1[0])

if __name__ == '__main__':
    frequencies = [[6, 2], [12, 2]]
    print(can_play_music(frequencies))

