
def get_input():
    n = int(input())
    p = list(map(int, input().split()))
    return n, p

def solve(n, p):
    count = 0
    for i in range(1, n-1):
        if p[i-1] < p[i] and p[i] < p[i+1]:
            count += 1
    return count

def main():
    n, p = get_input()
    print(solve(n, p))

if __name__ == '__main__':
    main()

