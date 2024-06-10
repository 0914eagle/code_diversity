
def get_heights():
    return list(map(int, input().split()))

def get_pairs(heights):
    n = len(heights)
    pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if abs(i - j) == sum(heights[i], heights[j]):
                pairs += 1
    return pairs

def main():
    heights = get_heights()
    pairs = get_pairs(heights)
    print(pairs)

if __name__ == '__main__':
    main()

