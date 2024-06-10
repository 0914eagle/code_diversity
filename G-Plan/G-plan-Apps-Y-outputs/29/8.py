
def minCoinsToSameCoordinate(n, chips):
    odd_count = sum(chip % 2 for chip in chips)
    return min(odd_count, n - odd_count)

if __name__ == "__main__":
    n = int(input())
    chips = list(map(int, input().split()))
    print(minCoinsToSameCoordinate(n, chips))
