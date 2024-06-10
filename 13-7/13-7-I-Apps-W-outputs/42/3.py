
def get_heights():
    return list(map(int, input().split()))

def get_num_pairs(heights):
    n = len(heights)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if abs(i - j) == sum(heights[i:j+1]):
                count += 1
    return count

def main():
    heights = get_heights()
    print(get_num_pairs(heights))

if __name__ == '__main__':
    main()

