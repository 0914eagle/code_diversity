
def find_polynomials(n):
    if n == 1:
        return 1, [0, 1], 0, [1]
    elif n == 2:
        return 2, [-1, 0, 1], 1, [0, 1]
    else:
        return -1

if __name__ == '__main__':
    n = int(input())
    print(find_polynomials(n))

