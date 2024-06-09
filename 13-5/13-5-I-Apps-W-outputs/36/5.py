
def get_bitwise_or(a, b):
    return a | b

def get_number_of_ways(n, heights):
    ways = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            height_sum = 0
            for k in range(i, j + 1):
                height_sum += heights[k]
            if get_bitwise_or(heights[i], heights[j]) < height_sum:
                ways += 1
    return ways

if __name__ == '__main__':
    n = int(input())
    heights = list(map(int, input().split()))
    print(get_number_of_ways(n, heights))

