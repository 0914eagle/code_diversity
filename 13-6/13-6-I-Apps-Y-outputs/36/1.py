
def solve(arr):
    n = len(arr)
    blocks = []
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == 0:
                blocks.append((i, j))
    return blocks

