
def get_blocks(arr):
    n = len(arr)
    blocks = []
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                blocks.append((i, j))
    return blocks

def find_maximum_set_of_disjoint_blocks(blocks):
    max_blocks = []
    for block in blocks:
        if block not in max_blocks:
            max_blocks.append(block)
    return max_blocks

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    blocks = get_blocks(arr)
    maximum_blocks = find_maximum_set_of_disjoint_blocks(blocks)
    print(len(maximum_blocks))
    for block in maximum_blocks:
        print(block[0], block[1])

if __name__ == '__main__':
    main()

