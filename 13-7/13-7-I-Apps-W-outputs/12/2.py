
def is_valid_x(x, N):
    for y in range(2, N+1):
        if x % y != 1:
            return False
    return True

def find_x(N):
    for x in range(N, 10**13):
        if is_valid_x(x, N):
            return x
    return -1

if __name__ == '__main__':
    N = int(input())
    x = find_x(N)
    print(x)

