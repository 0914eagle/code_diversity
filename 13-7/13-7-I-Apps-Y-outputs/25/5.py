
def get_input():
    return int(input())

def is_odd(num):
    return num % 2 != 0

def solve(N):
    count = 0
    for i in range(1, N + 1):
        if is_odd(i):
            count += 1
    return count / N

if __name__ == '__main__':
    N = get_input()
    print(solve(N))

