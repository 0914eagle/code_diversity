
def get_input():
    return int(input())

def count_odd_numbers_with_eight_divisors(n):
    count = 0
    for i in range(1, n+1):
        if i % 2 == 1 and len(list(set([1, i] + [j for j in range(1, int(i**0.5) + 1) if i % j == 0]))) == 8:
            count += 1
    return count

def main():
    n = get_input()
    print(count_odd_numbers_with_eight_divisors(n))

if __name__ == '__main__':
    main()

