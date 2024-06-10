
def get_input():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A

def find_max_diff(A):
    max_diff = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            diff = abs(A[i] - A[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff

def solve():
    N, A = get_input()
    max_diff = find_max_diff(A)
    print(max_diff)

if __name__ == '__main__':
    solve()

