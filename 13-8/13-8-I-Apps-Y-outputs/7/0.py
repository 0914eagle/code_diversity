
def get_input():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A

def solve(N, A):
    result = 1
    for i in range(N):
        result *= A[i]
    if result > 10**18:
        return -1
    else:
        return result

def main():
    N, A = get_input()
    print(solve(N, A))

if __name__ == '__main__':
    main()

