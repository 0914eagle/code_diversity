
def get_teammate(n, a):
    teammates = [-1] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if a[i][j] > a[j][i]:
                teammates[i] = j
                break
    return teammates

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    teammates = get_teammate(n, a)
    print(*teammates, sep='\n')

if __name__ == '__main__':
    main()

