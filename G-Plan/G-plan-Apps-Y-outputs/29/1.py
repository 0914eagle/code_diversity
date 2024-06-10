coins_to_same_coordinate(n, chips):
    odd_count = sum(chip % 2 for chip in chips)
    even_count = n - odd_count
    return min(odd_count, even_count)

if __name__ == "__main__":
    n = int(input())
    chips = list(map(int, input().split()))
    print(min_coins_to_same_coordinate(n, chips)