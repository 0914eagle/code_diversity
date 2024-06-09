
def get_sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

def count_integers_with_sum(a, b, s):
    count = 0
    for i in range(a, b+1):
        if get_sum_of_digits(i) == s:
            count += 1
    return count

def find_smallest_integer_with_sum(a, b, s):
    for i in range(a, b+1):
        if get_sum_of_digits(i) == s:
            return i
    return -1

if __name__ == '__main__':
    a, b, s = map(int, input().split())
    print(count_integers_with_sum(a, b, s))
    print(find_smallest_integer_with_sum(a, b, s))

