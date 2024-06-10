
def find_first_return_day(p):
    n = len(p)
    days = [0] * n
    for i in range(n):
        days[i] = 1
        for j in range(i+1, n):
            if p[i] == p[j]:
                days[i] += 1
                break
    return days

def main():
    q = int(input())
    for i in range(q):
        n = int(input())
        p = list(map(int, input().split()))
        days = find_first_return_day(p)
        print(*days)

if __name__ == '__main__':
    main()

