
def get_odd_numbers_with_eight_divisors(n):
    count = 0
    for i in range(1, n+1):
        if i % 2 != 0 and len(list(filter(lambda x: i % x == 0, range(1, int(i**0.5) + 1)))) == 8:
            count += 1
    return count

def main():
    n = int(input())
    print(get_odd_numbers_with_eight_divisors(n))

if __name__ == '__main__':
    main()

