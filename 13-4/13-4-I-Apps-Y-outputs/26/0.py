
def get_min_bar_size(k):
    # Find the smallest power of 2 that is greater than or equal to k
    power = 1
    while power < k:
        power *= 2
    return power

def get_min_breaks(k):
    # Find the number of breaks needed to obtain k squares
    power = get_min_bar_size(k)
    num_breaks = 0
    while power > k:
        power //= 2
        num_breaks += 1
    return num_breaks

if __name__ == '__main__':
    k = int(input())
    print(get_min_bar_size(k), get_min_breaks(k))

