
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve(n):
    count = 0
    for i in range(1, n + 1):
        if is_prime(i):
            count += 1
    return count

def input_data():
    return int(input())

def main():
    n = input_data()
    print(solve(n))

if __name__ == '__main__':
    main()

