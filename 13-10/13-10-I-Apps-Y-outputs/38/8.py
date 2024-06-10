
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_next_prime(x):
    while True:
        x += 1
        if is_prime(x):
            return x

def main():
    x = int(input())
    print(find_next_prime(x))

if __name__ == '__main__':
    main()

