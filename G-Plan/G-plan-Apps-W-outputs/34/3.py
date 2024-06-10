
MOD = 10**9 + 7

def is_valid_block(block, a, b):
    block_int = int(''.join(map(str, block)))
    return block_int % a == 0 and block[0] != b

def count_good_phone_numbers(n, k, a, b):
    count = 0
    for i in range(10 ** k):
        block = [int(d) for d in str(i).zfill(k)]
        if is_valid_block(block, a[i % (n // k)], b[i % (n // k)]):
            count += 1
    return count % MOD

if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = count_good_phone_numbers(n, k, a, b)
    print(result)
