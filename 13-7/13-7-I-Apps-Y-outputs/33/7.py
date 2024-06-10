
def get_blocks(arr):
    n = len(arr)
    blocks = []
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                blocks.append((i, j))
                break
    return blocks

def get_maximum_blocks(arr):
    n = len(arr)
    blocks = get_blocks(arr)
    max_blocks = []
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                max_blocks.append((i, j))
                break
    return max_blocks

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    blocks = get_maximum_blocks(arr)
    print(len(blocks))
    for block in blocks:
        print(block[0], block[1])

