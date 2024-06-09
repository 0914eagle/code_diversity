
def get_input():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A

def get_total_cost(N, A, i):
    total_cost = 0
    for j in range(N):
        if j != i:
            total_cost += abs(A[j] - A[j-1])
    return total_cost

def main():
    N, A = get_input()
    for i in range(N):
        print(get_total_cost(N, A, i))

if __name__ == '__main__':
    main()

