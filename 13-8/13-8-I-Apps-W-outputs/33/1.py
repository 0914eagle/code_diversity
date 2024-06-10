
def get_min_price(n, c1, c2, visitors):
    # Initialize variables
    min_price = float('inf')
    group_size = 1
    num_groups = 1

    # Iterate through possible group sizes
    for i in range(1, n + 1):
        group_size = i
        num_groups = n // group_size
        price = c1 + c2 * (group_size - 1) ** 2
        price *= num_groups
        if price < min_price:
            min_price = price

    return min_price

def main():
    n, c1, c2 = map(int, input().split())
    visitors = list(map(int, input()))
    print(get_min_price(n, c1, c2, visitors))

if __name__ == '__main__':
    main()

