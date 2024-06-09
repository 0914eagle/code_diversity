
def read_input():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    return N, K, Q, A

def find_min_diff(A, K, Q):
    min_diff = float('inf')
    for i in range(Q):
        subsequence = A[i:i+K]
        min_element = min(subsequence)
        max_element = max(subsequence)
        diff = max_element - min_element
        if diff < min_diff:
            min_diff = diff
    return min_diff

def main():
    N, K, Q, A = read_input()
    print(find_min_diff(A, K, Q))

if __name__ == '__main__':
    main()

