
def get_blocks(arr):
    n = len(arr)
    blocks = []
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                blocks.append((i, j))
    return blocks

def find_maximum_disjoint_blocks(arr):
    n = len(arr)
    blocks = get_blocks(arr)
    max_blocks = []
    for i in range(n):
        for j in range(i+1, n):
            block = (i, j)
            if block not in blocks:
                max_blocks.append(block)
    return max_blocks

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    blocks = find_maximum_disjoint_blocks(arr)
    print(len(blocks))
    for block in blocks:
        print(block[0], block[1])

