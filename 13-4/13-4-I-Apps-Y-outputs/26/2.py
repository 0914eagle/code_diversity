
def get_min_bar_size(k):
    # Find the smallest power of 2 that is greater than or equal to k
    power = 1
    while power < k:
        power *= 2
    return power

def get_min_breaks(k):
    # Find the smallest number of breaks needed to obtain k squares
    power = get_min_bar_size(k)
    breaks = 0
    while power > k:
        breaks += 1
        power //= 2
    return breaks

if __name__ == '__main__':
    k = int(input())
    print(get_min_bar_size(k), get_min_breaks(k))

