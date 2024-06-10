
def read_input():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    return N, A

def compute_xor(A, l, r):
    xor = 0
    for i in range(l, r+1):
        xor ^= A[i]
    return xor

def count_pairs(A, N):
    count = 0
    for l in range(1, N+1):
        for r in range(l, N+1):
            if compute_xor(A, l, r) == sum(A[l:r+1]):
                count += 1
    return count

def main():
    N, A = read_input()
    print(count_pairs(A, N))

if __name__ == '__main__':
    main()

