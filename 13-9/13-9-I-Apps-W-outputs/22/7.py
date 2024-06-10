
def get_xor_pairs(A):
    N = len(A)
    xor_pairs = 0
    for i in range(N):
        for j in range(i+1, N):
            xor = A[i] ^ A[j]
            if xor == A[i] + A[j]:
                xor_pairs += 1
    return xor_pairs

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(get_xor_pairs(A))

if __name__ == '__main__':
    main()

