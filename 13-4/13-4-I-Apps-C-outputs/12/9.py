
def get_digits(n):
    return [int(d) for d in str(n)]

def get_digit_sum(n):
    return sum(get_digits(n))

def count_integers(a, b, s):
    count = 0
    for i in range(a, b+1):
        if get_digit_sum(i) == s:
            count += 1
    return count

def find_smallest_integer(a, b, s):
    for i in range(a, b+1):
        if get_digit_sum(i) == s:
            return i
    return -1

if __name__ == '__main__':
    a, b, s = map(int, input().split())
    print(count_integers(a, b, s))
    print(find_smallest_integer(a, b, s))

