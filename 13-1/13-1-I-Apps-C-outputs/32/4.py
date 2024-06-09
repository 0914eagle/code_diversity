
def f1(N, M, K, measurements):
    # Initialize a 2D array to store the number of electrons with each spin
    num_electrons = [[0] * 2 for _ in range(N)]
    for y, x, spin in measurements:
        num_electrons[y - 1][spin == '+'] += 1
    
    # Initialize a set to store the valid states
    valid_states = set()
    
    # Iterate through each 2x2 subgrid
    for y in range(N):
        for x in range(M):
            for spin in range(2):
                # If the number of electrons with the current spin is even,
                # then the state is valid
                if num_electrons[y][spin] % 2 == 0:
                    valid_states.add((y, x, spin))
    
    return len(valid_states) % (10**9 + 7)

def f2(N, M, K, measurements):
    # Initialize a 2D array to store the number of electrons with each spin
    num_electrons = [[0] * 2 for _ in range(N)]
    for y, x, spin in measurements:
        num_electrons[y - 1][spin == '+'] += 1
    
    # Initialize a set to store the valid states
    valid_states = set()
    
    # Iterate through each 2x2 subgrid
    for y in range(N):
        for x in range(M):
            for spin in range(2):
                # If the number of electrons with the current spin is even,
                # then the state is valid
                if num_electrons[y][spin] % 2 == 0:
                    valid_states.add((y, x, spin))
    
    return len(valid_states) % (10**9 + 7)

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    measurements = []
    for _ in range(K):
        y, x, spin = input().split()
        measurements.append((int(y), int(x), spin))
    print(f1(N, M, K, measurements))
    print(f2(N, M, K, measurements))

