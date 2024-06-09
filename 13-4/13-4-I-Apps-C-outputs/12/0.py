
def get_digit_sum(n):
    return sum(int(d) for d in str(n))

def count_integers_with_digit_sum(a, b, s):
    count = 0
    for i in range(a, b+1):
        if get_digit_sum(i) == s:
            count += 1
    return count

def find_smallest_integer_with_digit_sum(a, b, s):
    for i in range(a, b+1):
        if get_digit_sum(i) == s:
            return i
    return -1

if __name__ == '__main__':
    a, b, s = map(int, input().split())
    print(count_integers_with_digit_sum(a, b, s))
    print(find_smallest_integer_with_digit_sum(a, b, s))

