
def get_permutation(n, q):
    permutation = [0] * n
    permutation[0] = 1
    for i in range(1, n):
        permutation[i] = permutation[i-1] + q[i-1]
    return permutation

def restore_permutation(n, q):
    permutation = get_permutation(n, q)
    if permutation[n-1] != n:
        return -1
    return permutation

if __name__ == '__main__':
    n = int(input())
    q = list(map(int, input().split()))
    print(*restore_permutation(n, q))

