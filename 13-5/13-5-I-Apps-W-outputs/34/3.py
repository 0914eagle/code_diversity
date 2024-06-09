
def is_sorted_in_column(table, l, r):
    for j in range(len(table[0])):
        for i in range(l, r):
            if table[i][j] > table[i+1][j]:
                return False
    return True

def solve(table, tasks):
    for l, r in tasks:
        if is_sorted_in_column(table[l-1:r], l, r):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    n, m = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]
    k = int(input())
    tasks = [list(map(int, input().split())) for _ in range(k)]
    solve(table, tasks)

