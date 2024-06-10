
def check_frequencies(frequencies):
    # Initialize a list to store the positions of the read/write heads
    positions = [0] * len(frequencies)
    
    # Iterate through each frequency and its intervals
    for i, (t_i, n_i) in enumerate(frequencies):
        # Iterate through each interval of the current frequency
        for j in range(n_i):
            # Calculate the start and end positions of the current interval
            start_pos = positions[i] + t_i * (j * 2)
            end_pos = positions[i] + t_i * (j * 2 + 1)
            
            # Check if the start and end positions are valid
            if start_pos >= 0 and end_pos <= 1000000:
                # Update the positions of the read/write heads
                positions[i] = end_pos
            else:
                return "impossible"
    
    # If all frequencies can be played as intended, return "possible"
    return "possible"

def main():
    f = int(input())
    frequencies = []
    for i in range(f):
        t_i, n_i = map(int, input().split())
        intervals = []
        for j in range(n_i):
            t_ij, t_i_j_plus_1 = map(int, input().split())
            intervals.append((t_ij, t_i_j_plus_1))
        frequencies.append((t_i, n_i, intervals))
    print(check_frequencies(frequencies))

if __name__ == '__main__':
    main()

