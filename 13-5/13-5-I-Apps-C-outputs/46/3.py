
def is_hill_number(n):
    if n < 10:
        return True
    
    prev_digit = None
    is_increasing = True
    for digit in str(n):
        if prev_digit is not None and prev_digit > digit:
            is_increasing = False
            break
        prev_digit = digit
    return is_increasing

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

