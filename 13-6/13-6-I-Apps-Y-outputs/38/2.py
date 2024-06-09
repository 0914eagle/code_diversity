
def get_input():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A

def get_cost(A, i):
    cost = 0
    for j in range(N):
        if j != i:
            cost += abs(A[j] - A[i])
    return cost

def main():
    N, A = get_input()
    for i in range(N):
        print(get_cost(A, i))

if __name__ == '__main__':
    main()

