
def check_possible(frequencies):
    # Initialize a list to store the positions of the read/write head for each frequency
    positions = [0] * len(frequencies)
    
    # Iterate through each frequency and its intervals
    for i, (t_i, n_i) in enumerate(frequencies):
        # Iterate through each interval for the current frequency
        for j in range(n_i):
            # Check if the current position of the read/write head is within the interval for the current frequency
            if positions[i] >= t_i[2*j] and positions[i] < t_i[2*j+1]:
                # If it is, move the read/write head to the end point of the radial axis
                positions[i] = t_i[2*j+1]
            else:
                # If it's not, move the read/write head to the start point of the radial axis
                positions[i] = t_i[2*j]
    
    # Check if all frequencies have reached the end point of the radial axis
    if all(position == t_i[2*n_i-1] for position, (t_i, n_i) in zip(positions, frequencies)):
        return "possible"
    else:
        return "impossible"

def main():
    f = int(input())
    frequencies = []
    for _ in range(f):
        t_i, n_i = map(int, input().split())
        t_i = [int(x) for x in input().split()]
        frequencies.append((t_i, n_i))
    print(check_possible(frequencies))

if __name__ == '__main__':
    main()

