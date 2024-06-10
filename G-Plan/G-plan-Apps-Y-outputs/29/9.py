
def minCoinsToSameCoordinate(n, chips):
    even_count = sum(chip % 2 == 0 for chip in chips)
    odd_count = n - even_count
    return min(even_count, odd_count)

if __name__ == "__main__":
    n = int(input())
    chips = list(map(int, input().split()))
    print(minCoinsToSameCoordinate(n, chips))
