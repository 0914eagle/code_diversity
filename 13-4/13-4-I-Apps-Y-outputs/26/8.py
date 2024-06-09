
def get_min_bar_size(k):
    # Find the smallest power of 2 greater than or equal to k
    bar_size = 1
    while bar_size < k:
        bar_size *= 2
    return bar_size

def get_min_breaks(k):
    # Find the smallest number of breaks needed to obtain k squares
    bar_size = get_min_bar_size(k)
    num_breaks = 0
    while bar_size > k:
        bar_size //= 2
        num_breaks += 1
    return num_breaks

if __name__ == '__main__':
    k = int(input())
    print(get_min_bar_size(k), get_min_breaks(k))

