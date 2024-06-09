
def get_digit_sum(n):
    return sum(int(d) for d in str(n))

def count_integers_with_digit_sum(A, B, S):
    count = 0
    for i in range(A, B+1):
        if get_digit_sum(i) == S:
            count += 1
    return count

def find_smallest_integer_with_digit_sum(A, B, S):
    for i in range(A, B+1):
        if get_digit_sum(i) == S:
            return i
    return -1

if __name__ == '__main__':
    A, B, S = map(int, input().split())
    print(count_integers_with_digit_sum(A, B, S))
    print(find_smallest_integer_with_digit_sum(A, B, S))

