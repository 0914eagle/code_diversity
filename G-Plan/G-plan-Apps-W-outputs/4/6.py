
def calculate_sadness(A):
    A.sort()
    median = A[len(A)//2]
    sadness = 0
    for i in range(len(A)):
        sadness += abs(A[i] - (median+i+1))
    return sadness

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    print(calculate_sadness(A))
