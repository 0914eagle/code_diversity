
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
            up, down = subgrid_counts[y][x]
            if up == down:
                valid_states.add((y, x, 0))
            if up + 1 == down:
                valid_states.add((y, x, 1))
            if up == down + 1:
                valid_states.add((y, x, -1))

    # Return the number of valid states modulo 10^9 + 7
    return len(valid_states) % (10**9 + 7)

def f2(N, M, K, measurements):
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
            up, down = subgrid_counts[y][x]
            if up == down:
                valid_states.add((y, x, 0))
            if up + 1 == down:
                valid_states.add((y, x, 1))
            if up == down + 1:
                valid_states.add((y, x, -1))

    # Return the number of valid states modulo 10^9 + 7
    return len(valid_states) % (10**9 + 7)

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    measurements = [input().split() for _ in range(K)]
    print(f1(N, M, K, measurements))
    print(f2(N, M, K, measurements))

