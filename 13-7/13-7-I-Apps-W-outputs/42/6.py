
def get_heights(n):
    return list(map(int, input().split()))

def get_pairs(heights):
    n = len(heights)
    pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if abs(i - j) == sum(heights[i:j+1]):
                pairs += 1
    return pairs

def main():
    n = int(input())
    heights = get_heights(n)
    print(get_pairs(heights))

if __name__ == '__main__':
    main()

