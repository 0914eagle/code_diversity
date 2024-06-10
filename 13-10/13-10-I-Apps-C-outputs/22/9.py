
def get_smallest_integer_for_function(b, n):
    # Find the smallest integer x such that f_b(x) = n
    x = 1
    while f_b(x) != n:
        x += 1
    return x

def f_b(x):
    # Calculate the value of f_b(x)
    sum = 0
    while x > 0:
        sum += x % b
        x //= b
    return sum

if __name__ == '__main__':
    b, n = map(int, input().split())
    print(get_smallest_integer_for_function(b, n))

