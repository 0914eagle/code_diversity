
MOD = 10**9 + 7

def is_valid_block(block, a, b):
    num = 0
    for i in range(len(block)):
        num += block[i] * 10**(len(block) - i - 1)
    return num % a == 0 and block[0] != b

def generate_phone_numbers(n, k, a, b):
    count = 0
    for i in range(10**(k)):
        block = [int(digit) for digit in str(i).zfill(k)]
        if is_valid_block(block, a, b):
            count += 1
    return count

def count_good_phone_numbers(n, k, a_list, b_list):
    total_count = 1
    for i in range(n // k):
        total_count *= generate_phone_numbers(n, k, a_list[i], b_list[i])
        total_count %= MOD
    return total_count

if __name__ == '__main__':
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    result = count_good_phone_numbers(n, k, a_list, b_list)
    print(result)
