
MOD = 10**9 + 7

def is_valid_block(block, a, b):
    num = 0
    for i in range(len(block)):
        num += block[i] * 10**(len(block) - i - 1)
    return num % a == 0 and block[0] != b

def count_good_phone_numbers(n, k, a, b):
    total_good_numbers = 1
    for i in range(n // k):
        valid_count = 0
        for num in range(10**k):
            block = [int(digit) for digit in str(num).zfill(k)]
            if is_valid_block(block, a[i], b[i]):
                valid_count += 1
        total_good_numbers = (total_good_numbers * valid_count) % MOD
    return total_good_numbers

if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    result = count_good_phone_numbers(n, k, a, b)
    print(result)
