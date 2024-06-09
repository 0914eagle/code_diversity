
def get_permutation(n, q):
    permutation = []
    for i in range(n):
        permutation.append(i+1)
    for i in range(n-1):
        if q[i] < 0 or q[i] > n-1:
            return [-1]
        for j in range(i+1, n):
            if permutation[j] == q[i]+i+1:
                permutation[j] = permutation[i]
                break
        permutation[i] = q[i]+i+1
    return permutation

def main():
    n = int(input())
    q = list(map(int, input().split()))
    permutation = get_permutation(n, q)
    if permutation == [-1]:
        print(-1)
    else:
        print(*permutation)

if __name__ == '__main__':
    main()

