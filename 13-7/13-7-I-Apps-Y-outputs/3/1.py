
def get_odd_digit_numbers(n):
    count = 0
    for i in range(1, n+1):
        if len(str(i)) % 2 == 1:
            count += 1
    return count

def main():
    n = int(input())
    print(get_odd_digit_numbers(n))

if __name__ == '__main__':
    main()

