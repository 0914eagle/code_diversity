
def get_permutation(n):
    permutation = list(range(1, n+1))
    for i in range(n):
        for j in range(i+1, n):
            if abs(permutation[i] - permutation[j]) not in range(2, 5):
                return -1
    return permutation

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(*get_permutation(n))

