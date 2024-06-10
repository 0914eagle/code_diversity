
def is_multiple_of_9(N):
    # Calculate the sum of digits of N
    digit_sum = sum(int(digit) for digit in str(N))
    
    # Check if the sum is divisible by 9
    if digit_sum % 9 == 0:
        return "Yes"
    else:
        return "No"

if __name__ == "__main__":
    N = int(input())
    result = is_multiple_of_9(N)
    print(result)
