
def get_subordinates(n, a):
    subordinates = [0] * (n + 1)
    for i in range(2, n + 1):
        subordinates[a[i - 1]] += 1
    return subordinates

def main():
    n = int(input())
    a = list(map(int, input().split()))
    subordinates = get_subordinates(n, a)
    for i in range(1, n + 1):
        print(subordinates[i])

if __name__ == '__main__':
    main()

