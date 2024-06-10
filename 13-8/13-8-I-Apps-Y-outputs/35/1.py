
def read_input():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A

def find_subordinates(N, A):
    subordinates = [0] * (N + 1)
    for i in range(2, N + 1):
        subordinates[A[i]] += 1
    return subordinates

def main():
    N, A = read_input()
    subordinates = find_subordinates(N, A)
    for i in range(1, N + 1):
        print(subordinates[i])

if __name__ == '__main__':
    main()

