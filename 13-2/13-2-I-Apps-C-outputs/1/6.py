
def count_integers_with_digit_sum(A, B, S):
    count = 0
    smallest = None
    for i in range(A, B+1):
        if sum(int(digit) for digit in str(i)) == S:
            count += 1
            if smallest is None or i < smallest:
                smallest = i
    return count, smallest

def main():
    A, B, S = map(int, input().split())
    count, smallest = count_integers_with_digit_sum(A, B, S)
    print(count)
    print(smallest)

if __name__ == '__main__':
    main()

