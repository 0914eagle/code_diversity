
def minCoinsToSameCoordinate(n, chips):
    even_count = 0
    odd_count = 0
    for chip in chips:
        if chip % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return min(even_count, odd_count)

if __name__ == "__main__":
    n = int(input())
    chips = list(map(int, input().split()))
    print(minCoinsToSameCoordinate(n, chips))
