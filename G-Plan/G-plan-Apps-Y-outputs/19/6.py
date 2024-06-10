
def is_multiple_of_9(n):
    # Check if the sum of digits is divisible by 9
    return sum(int(digit) for digit in str(n)) % 9 == 0

def main():
    n = int(input())
    if is_multiple_of_9(n):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
