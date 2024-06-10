
def get_input():
    return int(input())

def count_odd_digits(N):
    count = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 1:
            count += 1
    return count

def solve(N):
    return count_odd_digits(N)

if __name__ == '__main__':
    N = get_input()
    print(solve(N))

