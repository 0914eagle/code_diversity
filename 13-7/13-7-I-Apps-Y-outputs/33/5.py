
def get_blocks(a):
    n = len(a)
    blocks = []
    for i in range(n):
        for j in range(i+1, n):
            if a[i] + a[j] == a[i+1] + a[j+1]:
                blocks.append((i, j))
    return blocks

def get_maximum_blocks(a):
    blocks = get_blocks(a)
    max_blocks = []
    for i in range(len(blocks)):
        block = blocks[i]
        for j in range(i+1, len(blocks)):
            if block[0] <= blocks[j][0] and block[1] >= blocks[j][1]:
                break
        else:
            max_blocks.append(block)
    return max_blocks

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    blocks = get_maximum_blocks(a)
    print(len(blocks))
    for block in blocks:
        print(block[0], block[1])

