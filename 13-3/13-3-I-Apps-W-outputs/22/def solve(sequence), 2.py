
def solve(sequence):
    n = len(sequence)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if sequence[i] == (sequence[j] + sequence[i]) // 2:
                count += 1
                break
    return count

