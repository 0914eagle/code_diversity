
def is_multiple_of_9(N):
    # Check if the sum of digits is divisible by 9
    return sum(int(digit) for digit in str(N)) % 9 == 0

def data_inputer():
    # Read input from standard input
    N = int(input().strip())
    return N

if __name__ == "__main__":
    N = data_inputer()
    if is_multiple_of_9(N):
        print("Yes")
    else:
        print("No")
