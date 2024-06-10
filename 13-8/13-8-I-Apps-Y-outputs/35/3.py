
def get_input():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A

def get_subordinates(N, A):
    subordinates = [0] * (N + 1)
    for i in range(2, N + 1):
        subordinates[A[i]] += 1
    return subordinates

def main():
    N, A = get_input()
    subordinates = get_subordinates(N, A)
    for i in range(1, N + 1):
        print(subordinates[i])

if __name__ == '__main__':
    main()

