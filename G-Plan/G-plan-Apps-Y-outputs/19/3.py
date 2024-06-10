
def is_multiple_of_9(N):
    # Check if the sum of digits of N is divisible by 9
    digit_sum = sum(int(digit) for digit in str(N))
    return digit_sum % 9 == 0

def data_inputer():
    # Read input N
    N = int(input())
    return N

if __name__ == "__main__":
    N = data_inputer()
    if is_multiple_of_9(N):
        print("Yes")
    else:
        print("No")
