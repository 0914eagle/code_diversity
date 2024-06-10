
def read_input():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A

def xor_sum(A, l, r):
    return sum(A[l:r+1])

def xor_condition(A, l, r):
    return xor_sum(A, l, r) == A[l] + A[l+1]

def count_pairs(A):
    N = len(A)
    count = 0
    for l in range(N):
        for r in range(l, N):
            if xor_condition(A, l, r):
                count += 1
    return count

def main():
    N, A = read_input()
    print(count_pairs(A))

if __name__ == '__main__':
    main()

