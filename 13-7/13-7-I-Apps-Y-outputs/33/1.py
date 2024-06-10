
def get_blocks(arr):
    n = len(arr)
    blocks = []
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == arr[i+1] + arr[j+1]:
                blocks.append((i, j))
    return blocks

def get_maximum_blocks(blocks):
    max_blocks = []
    for block in blocks:
        if block not in max_blocks:
            max_blocks.append(block)
    return max_blocks

def get_blocks_output(blocks):
    output = []
    for block in blocks:
        output.append(str(block[0] + 1) + " " + str(block[1] + 1))
    return "\n".join(output)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    blocks = get_blocks(arr)
    max_blocks = get_maximum_blocks(blocks)
    print(len(max_blocks))
    print(get_blocks_output(max_blocks))

if __name__ == '__main__':
    main()

