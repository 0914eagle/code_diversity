
def solve(sequence):
    N = len(sequence)
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if sequence[i] == (sequence[j] + sequence[i]) // 2:
                count += 1
                break
    return count

