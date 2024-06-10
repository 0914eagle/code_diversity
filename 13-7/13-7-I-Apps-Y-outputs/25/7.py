
def get_input():
    return int(input())

def is_odd(n):
    return n % 2 == 1

def find_probability(n):
    odd_count = 0
    for i in range(1, n + 1):
        if is_odd(i):
            odd_count += 1
    return odd_count / n

def main():
    n = get_input()
    print(find_probability(n))

if __name__ == '__main__':
    main()

