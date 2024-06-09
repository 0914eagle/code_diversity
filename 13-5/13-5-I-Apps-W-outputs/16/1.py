
def get_digit_count(n):
    return len(str(n))

def solve(n):
    digit_count = 0
    for i in range(1, n+1):
        digit_count += get_digit_count(i)
    return digit_count

if __name__ == '__main__':
    n = int(input())
    print(solve(n))

