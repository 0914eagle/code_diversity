
def get_number_of_digits(n):
    return len(str(n))

def solve(n):
    return get_number_of_digits(n * (n + 1) // 2)

if __name__ == '__main__':
    n = int(input())
    print(solve(n))

