
def read_input():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A

def xor_bitwise(A, l, r):
    result = 0
    for i in range(l, r+1):
        result ^= A[i]
    return result

def count_pairs(A, N):
    count = 0
    for l in range(N):
        for r in range(l, N):
            if xor_bitwise(A, l, r) == sum(A[l:r+1]):
                count += 1
    return count

def main():
    N, A = read_input()
    print(count_pairs(A, N))

if __name__ == '__main__':
    main()

