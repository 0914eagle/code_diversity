
def is_hill_number(n):
    if n < 10:
        return True
    
    prev_digit = n % 10
    n //= 10
    
    while n > 0:
        curr_digit = n % 10
        if curr_digit < prev_digit:
            return False
        prev_digit = curr_digit
        n //= 10
    
    return True

def count_hill_numbers(n):
    count = 0
    for i in range(1, n+1):
        if is_hill_number(i):
            count += 1
    
    return count

def main():
    n = int(input())
    if is_hill_number(n):
        print(count_hill_numbers(n))
    else:
        print(-1)

if __name__ == '__main__':
    main()

