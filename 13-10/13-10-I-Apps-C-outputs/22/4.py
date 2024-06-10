
def get_digits(n):
    return [int(d) for d in str(n)]

def get_digit_product(n):
    return int(str(n)[0]) * int(str(n)[1])

def find_solution(b, n):
    for i in range(1, n+1):
        if get_digit_product(i) == n:
            return i
    return "impossible"

if __name__ == '__main__':
    b, n = map(int, input().split())
    print(find_solution(b, n))

