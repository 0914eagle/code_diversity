
def get_bitwise_or(x, y):
    return x | y

def get_pairs(heights):
    n = len(heights)
    pairs = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            if get_bitwise_or(heights[i], heights[j]) > max(heights[i:j+1]):
                pairs.append((i, j))
    return pairs

def main():
    n = int(input())
    heights = list(map(int, input().split()))
    print(len(get_pairs(heights)))

if __name__ == '__main__':
    main()

