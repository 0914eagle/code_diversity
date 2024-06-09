
def get_beautiful_table(n, k):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i + j == k:
                return [[i, j], [j, i]]
    return []

def main():
    n, k = map(int, input().split())
    table = get_beautiful_table(n, k)
    if table:
        for row in table:
            print(*row)
    else:
        print(-1)

if __name__ == '__main__':
    main()

