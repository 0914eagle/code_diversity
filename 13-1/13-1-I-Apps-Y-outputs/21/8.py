
def is_square(n):
    return int(n**0.5)**2 == n

def solve(a, b):
    concat = str(a) + str(b)
    return "Yes" if is_square(int(concat)) else "No"

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(solve(a, b))

