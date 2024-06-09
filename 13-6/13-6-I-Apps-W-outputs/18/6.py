
def get_criminals(n, a, t):
    criminals = 0
    for i in range(1, n+1):
        if t[i-1] == 1:
            if i == a:
                criminals += 1
            elif abs(i-a) == 1:
                criminals += 1
            elif abs(i-a) == 2:
                criminals += 1
    return criminals

def main():
    n, a = map(int, input().split())
    t = list(map(int, input().split()))
    print(get_criminals(n, a, t))

if __name__ == '__main__':
    main()

