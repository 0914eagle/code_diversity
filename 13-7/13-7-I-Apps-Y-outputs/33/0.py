
def get_input():
    n = int(input())
    arr = list(map(int, input().split()))
    return n, arr

def find_blocks(n, arr):
    blocks = []
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                blocks.append((i, j))
    return blocks

def solve(n, arr):
    blocks = find_blocks(n, arr)
    max_blocks = []
    for i in range(len(blocks)):
        block = blocks[i]
        for j in range(i+1, len(blocks)):
            if block[1] < blocks[j][0]:
                max_blocks.append(block)
                break
    return max_blocks

def main():
    n, arr = get_input()
    blocks = solve(n, arr)
    print(len(blocks))
    for block in blocks:
        print(block[0], block[1])

if __name__ == '__main__':
    main()

