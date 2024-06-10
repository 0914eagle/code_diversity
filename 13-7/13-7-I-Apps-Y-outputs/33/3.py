
def find_blocks(arr):
    n = len(arr)
    blocks = []
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                blocks.append((i, j))
                break
    return blocks

def print_blocks(blocks):
    print(len(blocks))
    for block in blocks:
        print(block[0], block[1])

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    blocks = find_blocks(arr)
    print_blocks(blocks)

