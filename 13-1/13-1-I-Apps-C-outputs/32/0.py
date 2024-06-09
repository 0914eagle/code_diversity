
def f1(N, M, K, measurements):
    # Initialize a 2D array to store the number of electrons with each spin
    num_electrons = [[0] * 2 for _ in range(N)]
    for measurement in measurements:
        y, x, spin = measurement
        num_electrons[y - 1][spin == '+'] += 1
    
    # Check if the number of electrons with each spin is equal in each 2x2 subgrid
    for i in range(N):
        for j in range(M):
            if num_electrons[i][0] != num_electrons[i][1]:
                return 0
    
    # If all subgrids have equal number of electrons with each spin, return the total number of valid states
    return (num_electrons[0][0] * num_electrons[0][1]) % (10**9 + 7)

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    measurements = []
    for _ in range(K):
        measurements.append(list(map(int, input().split())))
    print(f1(N, M, K, measurements))

