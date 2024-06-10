
def get_input():
    return int(input())

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 == 1

def count_pairs(k):
    count = 0
    for i in range(1, k + 1):
        for j in range(1, k + 1):
            if is_even(i) and is_odd(j):
                count += 1
    return count

def main():
    k = get_input()
    print(count_pairs(k))

if __name__ == '__main__':
    main()

