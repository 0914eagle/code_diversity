
def get_bitwise_or(a, b):
    return int(str(bin(a | b))[2:], 2)

def get_number_of_ways(n, heights):
    ways = 0
    for i in range(n):
        for j in range(i+1, n):
            if get_bitwise_or(heights[i], heights[j]) > max(heights[i:j+1]):
                ways += 1
    return ways

if __name__ == '__main__':
    n = int(input())
    heights = list(map(int, input().split()))
    print(get_number_of_ways(n, heights))

