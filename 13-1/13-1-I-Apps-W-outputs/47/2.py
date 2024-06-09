
def is_greek_number(n):
    if n == 1:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve(n):
    count = 0
    for i in range(1, n+1):
        if is_greek_number(i):
            count += 1
    return count

if __name__ == '__main__':
    n = int(input())
    print(solve(n))

