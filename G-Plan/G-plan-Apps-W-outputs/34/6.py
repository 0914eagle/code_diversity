
MOD = 10**9 + 7

def is_valid_block(block, a, b):
    block_int = int(''.join(str(d) for d in block))
    return block_int % a == 0 and block[0] != b

def count_good_phone_numbers(n, k, a, b):
    count = 0
    for i in range(10):
        for j in range(10):
            for x in range(10):
                for y in range(10):
                    phone_number = [i, j, x, y]
                    valid = True
                    for idx in range(n // k):
                        block = phone_number[idx*k:(idx+1)*k]
                        if not is_valid_block(block, a[idx], b[idx]):
                            valid = False
                            break
                    if valid:
                        count += 1
    return count % MOD

if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = count_good_phone_numbers(n, k, a, b)
    print(result)
