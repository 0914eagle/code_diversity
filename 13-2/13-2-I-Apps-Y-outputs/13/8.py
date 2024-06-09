
def solve(sequence, k):
    n = len(sequence)
    if k > n:
        return -1
    
    sequence.sort()
    for i in range(1, 10**9):
        count = 0
        for j in range(n):
            if sequence[j] <= i:
                count += 1
                if count == k:
                    return i
    
    return -1

