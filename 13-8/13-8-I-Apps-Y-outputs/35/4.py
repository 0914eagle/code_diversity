
def read_input():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A

def find_subordinates(A):
    subordinates = [0] * len(A)
    for i in range(1, len(A)):
        subordinates[A[i] - 1] += 1
    return subordinates

def main():
    N, A = read_input()
    subordinates = find_subordinates(A)
    for i in range(len(subordinates)):
        print(subordinates[i])

if __name__ == '__main__':
    main()

