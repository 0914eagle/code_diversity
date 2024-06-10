
def get_max_diff(A):
    n = len(A)
    max_diff = 0
    for i in range(n-1):
        for j in range(i+1, n):
            diff = abs(A[i] - A[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff

def main():
    n = int(input())
    A = list(map(int, input().split()))
    print(get_max_diff(A))

if __name__ == '__main__':
    main()

