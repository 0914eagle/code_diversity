
def get_correct_codes(N, M, C, B, A):
    correct_codes = 0
    for i in range(N):
        sum = 0
        for j in range(M):
            sum += A[i][j] * B[j]
        if sum + C > 0:
            correct_codes += 1
    return correct_codes

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    correct_codes = get_correct_codes(N, M, C, B, A)
    print(correct_codes)

if __name__ == '__main__':
    main()

