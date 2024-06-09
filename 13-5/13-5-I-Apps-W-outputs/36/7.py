
def get_bitwise_or(x, y):
    return x | y

def get_number_of_ways(n, heights):
    number_of_ways = 0
    for i in range(n):
        for j in range(i+1, n):
            height_between_mountains = 0
            for k in range(i, j+1):
                height_between_mountains |= heights[k]
            if height_between_mountains > heights[i] and height_between_mountains > heights[j]:
                number_of_ways += 1
    return number_of_ways

if __name__ == '__main__':
    n = int(input())
    heights = list(map(int, input().split()))
    print(get_number_of_ways(n, heights))

