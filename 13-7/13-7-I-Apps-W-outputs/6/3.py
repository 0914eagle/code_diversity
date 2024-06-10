
def is_lovely(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_biggest_lovely_number(n):
    lovely_numbers = []
    for i in range(1, n + 1):
        if is_lovely(i):
            lovely_numbers.append(i)
    return max(lovely_numbers)

if __name__ == '__main__':
    n = int(input())
    print(get_biggest_lovely_number(n))

