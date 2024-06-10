
def get_permutation(n, q):
    permutation = []
    for i in range(n):
        permutation.append(i+1)
    for i in range(n-1):
        for j in range(n-i-1):
            if q[i] < q[j]:
                permutation[i], permutation[j] = permutation[j], permutation[i]
    return permutation

def main():
    n = int(input())
    q = list(map(int, input().split()))
    permutation = get_permutation(n, q)
    if permutation is None:
        print(-1)
    else:
        print(*permutation)

if __name__ == '__main__':
    main()

