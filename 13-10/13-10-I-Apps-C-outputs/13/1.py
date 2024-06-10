
def get_sum_of_sizes(guests, size):
    return sum(guest for guest in guests if guest <= size)


def get_average_number_of_visitors(n, a, p):
    guests = iter(a)
    total_number_of_visitors = 0
    for i in range(n):
        guest = next(guests)
        if get_sum_of_sizes(guests, p - guest) >= guest:
            total_number_of_visitors += 1
    return total_number_of_visitors / n


if __name__ == '__main__':
    n = int(input())
    a = tuple(map(int, input().split()))
    p = int(input())
    print(get_average_number_of_visitors(n, a, p))

