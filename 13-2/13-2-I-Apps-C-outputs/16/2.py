
def find_carryless_square_root(n):
    for i in range(1, n+1):
        if i * i == n:
            return i
    return -1

if __name__ == '__main__':
    n = int(input())
    print(find_carryless_square_root(n))

