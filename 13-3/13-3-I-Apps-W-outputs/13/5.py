
def f1(n, k, a, b):
    # Calculate the number of good phone numbers
    count = 0
    for i in range(10**n):
        # Convert the phone number to a list of digits
        num = list(str(i))
        # Check if the phone number is good
        if is_good(num, k, a, b):
            count += 1
    return count % (10**9 + 7)

def is_good(num, k, a, b):
    # Split the phone number into blocks of length k
    blocks = [num[i:i+k] for i in range(0, len(num), k)]
    # Check if the blocks are divisible by a and don't start with b
    for i, block in enumerate(blocks):
        if int(''.join(block)) % a[i] != 0 or block[0] == str(b[i]):
            return False
    return True

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(f1(n, k, a, b))

