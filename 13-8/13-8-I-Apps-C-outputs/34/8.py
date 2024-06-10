
def is_possible(frequencies):
    # Initialize a list to store the intervals for each frequency
    intervals = []
    for frequency in frequencies:
        intervals.append([])
    
    # Iterate over the intervals for each frequency
    for i in range(len(frequencies)):
        for j in range(0, len(frequencies[i]), 2):
            # Add the interval to the list of intervals for the corresponding frequency
            intervals[i].append((frequencies[i][j], frequencies[i][j+1]))
    
    # Sort the intervals for each frequency by their start time
    for i in range(len(frequencies)):
        intervals[i].sort(key=lambda x: x[0])
    
    # Check if the intervals for each frequency are non-overlapping
    for i in range(len(frequencies)):
        for j in range(len(frequencies[i])-1):
            if intervals[i][j][1] > intervals[i][j+1][0]:
                return "impossible"
    
    return "possible"

def main():
    f = int(input())
    frequencies = []
    for i in range(f):
        t, n = map(int, input().split())
        frequencies.append(list(map(int, input().split())))
    
    print(is_possible(frequencies))

if __name__ == '__main__':
    main()

