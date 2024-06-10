
def get_digit_sum(n):
    return sum(int(i) for i in str(n))

def solve(n):
    if n == 0:
        return 0
    else:
        return get_digit_sum(n) % 2

if __name__ == '__main__':
    n = int(input())
    print(solve(n))

