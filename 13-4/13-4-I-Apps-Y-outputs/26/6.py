
def get_bar_size(k):
    # Find the smallest power of 2 greater than or equal to k
    power = 1
    while power < k:
        power *= 2
    return power

def get_number_of_breaks(k):
    # Find the number of breaks needed to get k squares
    power = get_bar_size(k)
    number_of_breaks = 0
    while power > k:
        power //= 2
        number_of_breaks += 1
    return number_of_breaks

def get_smallest_bar_size(k):
    # Find the smallest bar size that has at least k squares
    power = 1
    while power < k:
        power *= 2
    return power

if __name__ == '__main__':
    k = int(input())
    print(get_smallest_bar_size(k), get_number_of_breaks(k))

