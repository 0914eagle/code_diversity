
def get_odd_digits(n):
    count = 0
    for i in range(1, n+1):
        if len(str(i)) % 2 == 1:
            count += 1
    return count

def solve(n):
    return get_odd_digits(n)

if __name__ == '__main__':
    n = int(input())
    print(solve(n))

