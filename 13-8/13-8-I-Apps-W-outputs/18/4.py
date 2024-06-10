
def is_lovely(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_biggest_lovely_number(n):
    for i in range(n, 1, -1):
        if is_lovely(i):
            return i
    return 0

if __name__ == '__main__':
    n = int(input())
    print(get_biggest_lovely_number(n))

