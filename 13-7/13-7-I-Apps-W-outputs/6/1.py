
def is_lovely(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_max_lovely(n):
    max_lovely = 0
    for i in range(1, n+1):
        if is_lovely(i):
            max_lovely = max(max_lovely, i)
    return max_lovely

if __name__ == '__main__':
    n = int(input())
    print(find_max_lovely(n))

