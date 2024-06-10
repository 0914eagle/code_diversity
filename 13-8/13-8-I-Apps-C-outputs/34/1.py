
def check_frequencies(frequencies):
    # Initialize a list to store the play times for each frequency
    play_times = []
    
    # Iterate over the frequencies
    for frequency in frequencies:
        # Initialize a list to store the play times for this frequency
        frequency_play_times = []
        
        # Iterate over the intervals for this frequency
        for interval in frequency:
            # Add the start and end times for this interval to the list of play times for this frequency
            frequency_play_times.append(interval[0])
            frequency_play_times.append(interval[1])
        
        # Sort the list of play times for this frequency in ascending order
        frequency_play_times.sort()
        
        # Add the list of play times for this frequency to the overall list of play times
        play_times.append(frequency_play_times)
    
    # Sort the overall list of play times in ascending order
    play_times.sort()
    
    # Initialize a flag to indicate whether all frequencies can be played as intended
    all_playable = True
    
    # Iterate over the lists of play times for each frequency
    for i in range(len(play_times)):
        # Iterate over the play times for this frequency
        for j in range(len(play_times[i])):
            # If the play time for this frequency is not equal to the corresponding play time in the overall list of play times, set the flag to False
            if play_times[i][j] != play_times[j]:
                all_playable = False
                break
        
        # If the flag has been set to False, break out of the inner loop
        if not all_playable:
            break
    
    # Return the flag indicating whether all frequencies can be played as intended
    return all_playable

def main():
    # Read the number of frequencies
    num_frequencies = int(input())
    
    # Initialize a list to store the frequencies
    frequencies = []
    
    # Iterate over the frequencies
    for i in range(num_frequencies):
        # Read the number of intervals for this frequency and the intervals themselves
        num_intervals = int(input())
        intervals = []
        for j in range(num_intervals):
            intervals.append(list(map(int, input().split())))
        
        # Add the frequency and its intervals to the list of frequencies
        frequencies.append(intervals)
    
    # Check if all frequencies can be played as intended
    if check_frequencies(frequencies):
        print("possible")
    else:
        print("impossible")

if __name__ == '__main__':
    main()

