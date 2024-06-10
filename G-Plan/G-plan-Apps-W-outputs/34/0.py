
def is_valid_block(block, a, b):
    block_int = int(''.join(map(str, block)))
    return block_int % a == 0 and block[0] != b

def generate_phone_numbers(n, k, a, b):
    count = 0
    for i in range(10 ** n):
        phone_number = list(map(int, str(i).zfill(n)))
        blocks = [phone_number[j:j+k] for j in range(0, n, k)]
        if all(is_valid_block(block, a[idx], b[idx]) for idx, block in enumerate(blocks)):
            count += 1
    return count % (10**9 + 7)

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = generate_phone_numbers(n, k, a, b)
    print(result)
