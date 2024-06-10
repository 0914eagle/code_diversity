
def get_multiple_of_k(k):
    # find the smallest possible sum of the digits in the decimal notation of a positive multiple of k
    return sum(str(k))

def get_smallest_sum_of_digits(k):
    # find the smallest possible sum of the digits in the decimal notation of a positive multiple of k
    smallest_sum = float('inf')
    for i in range(1, 10**5):
        if i % k == 0:
            sum_of_digits = get_multiple_of_k(i)
            if sum_of_digits < smallest_sum:
                smallest_sum = sum_of_digits
    return smallest_sum

if __name__ == '__main__':
    k = int(input())
    print(get_smallest_sum_of_digits(k))

