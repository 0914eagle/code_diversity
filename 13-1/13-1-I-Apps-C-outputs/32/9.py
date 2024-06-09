
def f1(N, M, K, measurements):
    # Initialize a 2D array to store the number of up and down spins in each subgrid
    subgrid_counts = [[[0, 0] for _ in range(N)] for _ in range(M)]

    # Iterate over the measurements and update the subgrid counts
    for measurement in measurements:
        y, x, spin = measurement
        subgrid_counts[y - 1][x - 1][0 if spin == "+" else 1] += 1

    # Initialize a set to store the valid states
    valid_states = set()

    # Iterate over the subgrids and check if they are consistent with the measurements
    for y in range(N):
        for x in range(M):
            up_count, down_count = subgrid_counts[y][x]
            if up_count == down_count:
                valid_states.add((y, x, up_count))

    # Return the number of valid states modulo 10^9 + 7
    return len(valid_states) % (10**9 + 7)

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    measurements = [input().split() for _ in range(K)]
    print(f1(N, M, K, measurements))

