
def f1(N, M, K, measurements):
    # Initialize a 2D array to store the number of electrons with each spin
    num_electrons = [[0] * 2 for _ in range(N)]
    for y, x, s in measurements:
        num_electrons[y - 1][s == '+'] += 1
    
    # Initialize a set to store the valid states
    valid_states = set()
    
    # Iterate through each 2x2 subgrid
    for y in range(N):
        for x in range(M):
            for s in range(2):
                # If the number of electrons with the current spin is even, add the state to the valid states set
                if num_electrons[y][s] % 2 == 0:
                    valid_states.add((y, x, s))
    
    return len(valid_states) % (10**9 + 7)

def f2(N, M, K, measurements):
    # Initialize a 2D array to store the number of electrons with each spin
    num_electrons = [[0] * 2 for _ in range(N)]
    for y, x, s in measurements:
        num_electrons[y - 1][s == '+'] += 1
    
    # Initialize a set to store the valid states
    valid_states = set()
    
    # Iterate through each 2x2 subgrid
    for y in range(N):
        for x in range(M):
            for s in range(2):
                # If the number of electrons with the current spin is even, add the state to the valid states set
                if num_electrons[y][s] % 2 == 0:
                    valid_states.add((y, x, s))
    
    return len(valid_states) % (10**9 + 7)

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    measurements = [input().split() for _ in range(K)]
    print(f1(N, M, K, measurements))
    print(f2(N, M, K, measurements))

