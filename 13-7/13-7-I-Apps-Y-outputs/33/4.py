
def get_blocks(arr):
    n = len(arr)
    blocks = []
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                blocks.append((i, j))
    return blocks

def get_maximum_blocks(arr):
    blocks = get_blocks(arr)
    max_blocks = []
    for block in blocks:
        if len(max_blocks) == 0:
            max_blocks.append(block)
        else:
            is_valid = True
            for existing_block in max_blocks:
                if block[0] <= existing_block[1] and block[1] >= existing_block[0]:
                    is_valid = False
                    break
            if is_valid:
                max_blocks.append(block)
    return max_blocks

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    blocks = get_maximum_blocks(arr)
    print(len(blocks))
    for block in blocks:
        print(block[0], block[1])

if __name__ == '__main__':
    main()

