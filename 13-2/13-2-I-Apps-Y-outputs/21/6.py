
def restore_permutation(n, q):
    permutation = []
    for i in range(n):
        permutation.append(i+1)
    for i in range(n-1):
        if q[i] >= 0:
            permutation[i+1] = permutation[i] + q[i]
        else:
            permutation[i] = permutation[i+1] + q[i]
    return permutation

def main():
    n = int(input())
    q = list(map(int, input().split()))
    permutation = restore_permutation(n, q)
    if permutation == []:
        print(-1)
    else:
        print(*permutation)

if __name__ == '__main__':
    main()

