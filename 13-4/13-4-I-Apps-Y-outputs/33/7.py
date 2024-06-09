
def solve(N, X, L):
    count = 0
    for i in range(N+1):
        if i == 0:
            coordinate = 0
        else:
            coordinate = coordinate + L[i-1]
        if coordinate <= X:
            count += 1
    return count

