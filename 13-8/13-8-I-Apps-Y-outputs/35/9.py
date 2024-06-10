
def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def get_subordinates(n, a):
    subordinates = [0] * n
    for i in range(2, n+1):
        subordinates[a[i-1]-1] += 1
    return subordinates

def main():
    n, a = get_input()
    subordinates = get_subordinates(n, a)
    for i in range(n):
        print(subordinates[i])

if __name__ == '__main__':
    main()

