
def find_smallest_sum_of_digits(k):
    # find the smallest possible multiple of k
    multiple = k
    while True:
        if sum_of_digits(multiple) <= sum_of_digits(multiple + 1):
            break
        multiple += k
    return multiple

def sum_of_digits(n):
    # sum the digits of n
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

if __name__ == '__main__':
    k = int(input())
    print(find_smallest_sum_of_digits(k))

