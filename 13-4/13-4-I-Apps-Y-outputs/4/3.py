
def solve():
    N = int(input())
    permutation = list(map(int, input().split()))

    count = 0
    for i in range(N):
        for j in range(i):
            if permutation[i] <= permutation[j]:
                break
        else:
            count += 1

    return count

