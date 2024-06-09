
def find_beautiful_table(n, k):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i + j == k:
                return [i, j]
    return []

def main():
    n, k = map(int, input().split())
    table = find_beautiful_table(n, k)
    if table:
        print(table[0], table[1])
    else:
        print(-1)

if __name__ == '__main__':
    main()

