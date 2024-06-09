
def get_bar_size(k):
    # Find the smallest power of 2 greater than or equal to k
    bar_size = 1
    while bar_size < k:
        bar_size *= 2
    return bar_size

def get_number_of_breaks(k):
    # Find the number of breaks needed to obtain k squares
    bar_size = get_bar_size(k)
    number_of_breaks = 0
    while bar_size > k:
        bar_size //= 2
        number_of_breaks += 1
    return number_of_breaks

def get_smallest_bar_size(k):
    # Find the smallest bar size that has at least k squares
    bar_size = 1
    while bar_size < k:
        bar_size *= 2
    return bar_size

def main():
    k = int(input())
    print(get_smallest_bar_size(k), get_number_of_breaks(k))

if __name__ == '__main__':
    main()

