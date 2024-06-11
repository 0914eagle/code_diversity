
def is_multiple_of_9(N):
    total = sum(int(digit) for digit in str(N))
    return total % 9 == 0

def main():
    N = int(input())
    if is_multiple_of_9(N):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()