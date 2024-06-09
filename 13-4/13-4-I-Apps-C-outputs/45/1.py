
import math

def get_special_numbers(n, k):
    count = 0
    for i in range(1, n+1):
        binary = bin(i)[2:]
        set_bits = binary.count('1')
        if set_bits == k:
            count += 1
    return count

def main():
    n = int(input())
    k = int(input())
    print(get_special_numbers(n, k) % (10**9 + 7))

if __name__ == '__main__':
    main()

