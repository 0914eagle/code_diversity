
def is_multiple_of_9(N):
    # Check if the sum of digits of N is divisible by 9
    digit_sum = sum(int(digit) for digit in str(N))
    return digit_sum % 9 == 0

def main():
    N = int(input())
    if is_multiple_of_9(N):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
