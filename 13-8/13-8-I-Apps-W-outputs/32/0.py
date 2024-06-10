
def get_comfort(a):
    n = len(a)
    comfort = 0
    for i in range(n):
        for j in range(i+1, n):
            comfort ^= a[j]
    return comfort

def get_max_comfort(a):
    n = len(a)
    max_comfort = 0
    for i in range(n):
        for j in range(i+1, n):
            max_comfort = max(max_comfort, get_comfort(a[i:j+1]))
    return max_comfort

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_max_comfort(a))

if __name__ == '__main__':
    main()

