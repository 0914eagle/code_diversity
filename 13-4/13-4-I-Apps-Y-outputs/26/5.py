
def get_smallest_bar_size(k):
    # Find the smallest power of 2 greater than or equal to k
    power = 1
    while power < k:
        power *= 2
    return power

def get_min_breaks(k):
    # Get the smallest bar size that has at least k squares
    bar_size = get_smallest_bar_size(k)

    # Calculate the number of breaks needed to get k squares
    num_breaks = 0
    while bar_size > k:
        num_breaks += 1
        bar_size //= 2

    return num_breaks

def main():
    k = int(input())
    print(get_smallest_bar_size(k), get_min_breaks(k))

if __name__ == '__main__':
    main()

