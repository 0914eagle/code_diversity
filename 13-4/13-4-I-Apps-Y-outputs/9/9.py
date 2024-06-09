
def get_input():
    return int(input())

def is_valid_tuple(a, b, c, n):
    return a > 0 and b > 0 and c > 0 and a * b + c == n

def count_valid_tuples(n):
    count = 0
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            c = n - a * b
            if is_valid_tuple(a, b, c, n):
                count += 1
    return count

if __name__ == '__main__':
    n = get_input()
    print(count_valid_tuples(n))

