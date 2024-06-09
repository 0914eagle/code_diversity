
def get_sum(A, i, j):
    if i > len(A) or j > len(A[0]):
        return -1
    return A[i - 1][j - 1]

def get_max_sum(A, L):
    max_sum = -1
    for i in range(len(A)):
        for j in range(len(A[0])):
            sum1 = get_sum(A, i, j)
            sum2 = get_sum(A, j, i)
            if sum1 != -1 and sum2 != -1:
                max_sum = max(max_sum, sum1 + sum2)
    return max_sum

def main():
    N, M = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    L = int(input())
    print(get_max_sum(A, L))

if __name__ == '__main__':
    main()

