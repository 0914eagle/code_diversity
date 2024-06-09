
def solve():
    N = int(input())
    permutation = list(map(int, input().split()))
    count = 0
    for i in range(1, N+1):
        for j in range(1, i):
            if permutation[i-1] <= permutation[j-1]:
                break
        else:
            count += 1
    return count

