
def get_input():
    return int(input())

def is_valid_tuple(n, a, b, c):
    return a > 0 and b > 0 and c > 0 and a * b + c == n

def count_tuples(n):
    count = 0
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                if is_valid_tuple(n, a, b, c):
                    count += 1
    return count

if __name__ == '__main__':
    n = get_input()
    print(count_tuples(n))

