
def find_blocks(arr):
    n = len(arr)
    blocks = []
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                blocks.append((i, j))
                break
    return blocks

