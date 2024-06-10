
def find_blocks(a):
    n = len(a)
    blocks = []
    for i in range(n):
        for j in range(i+1, n):
            if a[i] == a[j]:
                blocks.append((i, j))
    return blocks

def solve(a):
    n = len(a)
    blocks = find_blocks(a)
    max_blocks = []
    for i in range(n):
        for j in range(i+1, n):
            if a[i] == a[j]:
                max_blocks.append((i, j))
    return max_blocks

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))

