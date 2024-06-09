
def find_permutation(n):
    permutation = list(range(1, n+1))
    for i in range(n-1):
        for j in range(i+1, n):
            if abs(permutation[i] - permutation[j]) not in range(2, 5):
                return -1
    return permutation

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        permutation = find_permutation(n)
        if permutation == -1:
            print(-1)
        else:
            print(*permutation)

if __name__ == '__main__':
    main()

