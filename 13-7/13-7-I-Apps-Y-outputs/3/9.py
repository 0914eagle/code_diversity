
def get_input():
    return int(input())

def count_odd_digits(n):
    count = 0
    for i in range(1, n+1):
        if len(str(i)) % 2 == 1:
            count += 1
    return count

def solve(n):
    return count_odd_digits(n)

if __name__ == '__main__':
    n = get_input()
    print(solve(n))

