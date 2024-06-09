
def is_squarefree(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_m(n):
    for m in range(2, n):
        if is_squarefree(m * n):
            return m
    return -1

if __name__ == '__main__':
    n = int(input())
    m = find_m(n)
    print(m)

